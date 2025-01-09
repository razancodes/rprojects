import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout, QLineEdit,QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import requests


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.welcome_label=QLabel("Weather App",self)
        self.city_label=QLabel("Please enter a City Name: ",self)
        self.city_input=QLineEdit(self)
        self.weather_button=QPushButton("Search",self)
        self.temperature_label=QLabel()
        self.emoji_label=QLabel()
        self.description_label=QLabel()
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Razans Weather App")
        self.setWindowIcon(QIcon(r"C:\Users\MRaza\Downloads\weather-symbol-7-svgrepo-com.svg"))
        self.setGeometry(700,300,512,512)


        vbox=QVBoxLayout()
        qhbox1=QHBoxLayout()
        vbox.addWidget(self.welcome_label)
        qhbox1.addWidget(self.city_label)
        qhbox1.addWidget(self.city_input)
        vbox.addLayout(qhbox1)
        vbox.addWidget(self.weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        
        self.welcome_label.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.setLayout(vbox)
        vbox.setSpacing(10)
        #self.setStyleSheet("background-color: #a2d6d6;")


        self.welcome_label.setStyleSheet("color: #103f4a;""font-size: 50px;""font-family: SF Pro Display;""font-weight: bold;")
        self.city_label.setStyleSheet("color: #103f4a;""font-size: 20px;""font-family: SF Pro Display;")
        self.city_input.setStyleSheet("color: #103f4a;""font-size: 20px;""font-family: SF Pro Display;""font-weight: bold;")
        self.temperature_label.setStyleSheet("color: #103f4a;""font-size: 50px;""font-family: SF Pro Display;")
        self.description_label.setStyleSheet("color: #103f4a;""font-size: 50px;""font-family: SF Pro Display;")
        self.emoji_label.setStyleSheet("color: #103f4a;""font-size: 150px;""font-family: SF Pro Display;""padding-bottom: 10px")
        self.weather_button.setStyleSheet("color: #103f4a;""font-size: 20px;""font-family: SF Pro Display;")

        self.weather_button.clicked.connect(self.get_weather)
        
    def get_weather(self):
        api_keys="d7369d16fb0a5526d871fa85f0b3c698"
        city=self.city_input.text()
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_keys}"

        try: 
            response=requests.get(url)
            response.raise_for_status()
            data=response.json()
            if data["cod"]==200:
                self.display_weather(data)
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.Display_error("Bad request:\nPlease check your input")
                case 401:
                    self.Display_error("Unauthorized:\nInvalid API key")
                case 403:
                    self.Display_error("Forbidden:\nAccess is denied")
                case 404:
                    self.Display_error("Not found:\nCity not found")
                case 500:
                    self.Display_error("Internal Server Error:\nPlease try again later")
                case 502:
                    self.Display_error("Bad Gateway:\nInvalid response from the server")
                case 503:
                    self.Display_error("Service Unavailable:\nServer is down")
                case 504:
                    self.Display_error("Gateway Timeout:\nNo response from the server")
                case _:
                    self.Display_error(f"HTTP error occurred:\n{http_error}")
            
        except requests.exceptions.ConnectionError:
            self.Display_error("Connection Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.Display_error("Timeout Error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.Display_error("Too many Redirects:\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            self.Display_error(f"Request Error:\n{req_error}")

    def Display_error(self, message):
        # Create and configure the QMessageBox
        self.temperature_label.setStyleSheet("color: #103f4a;""font-size: 30px;""font-family: SF Pro Display")
        self.description_label.setStyleSheet("color: #103f4a;""font-size: 30px;""font-family: SF Pro Display")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()
    def display_weather(self,data):
        self.description_label.setStyleSheet("color: #103f4a;""font-size: 50px;""font-family: SF Pro Display;""padding-bottom: 5px;")
        self.temperature_label.setStyleSheet("border-radius: 5px;""color: #103f4a;""font-size: 50px;""font-family: SF Pro Display;")
        
        temperature_k=data["main"]["temp"]
        temperature_c=round(temperature_k-273.15)
        temperature_f=round((temperature_k*9/5)-459.67)
        weather_id=data["weather"][0]["id"]

        weather_description=data["weather"][0]["description"]
        self.description_label.setText(weather_description)
        self.emoji_label.setText(self.get_weather_icon(weather_id))
        self.temperature_label.setText(f"{temperature_c}°C")

    def get_weather_icon(self,weather_id):
        if 200 <= weather_id <= 232:
             return "⛈"
        elif 300 <= weather_id <= 321:
            return "🌦"
        elif 500 <= weather_id <= 531:
            return "🌧"
        elif 600 <= weather_id <= 622:
            return "❄"
        elif 701 <= weather_id <= 741:
            return "🌫"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪"
        elif weather_id == 800:
            return "☀"
        elif 801 <= weather_id <= 804:
            return "☁"
        else:
            return ""

        
if __name__=="__main__":
    app=QApplication(sys.argv)
    Weather_app=WeatherApp()
    Weather_app.show()
    sys.exit(app.exec_())