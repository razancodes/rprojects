import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QGridLayout,QVBoxLayout,QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
class TicTacToeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.buttons=[[QPushButton(" ") for i in range(3)]for j in range(3)]
        self.initUI()
        self.functionality()
        self.row_count={"X":[0,0,0],"O":[0,0,0]}
        self.column_count={"X":[0,0,0],"O":[0,0,0]}
        self.diagonal_count={"X":[0],"O":[0]}
        self.antidiagonal_count={"X":[0],"O":[0]}
        self.player="X"
        self.i=0

    def initUI(self):
        self.setWindowTitle("Razans Tic Tac Toe")
        self.setWindowIcon(QIcon(r"C:\Users\MRaza\Downloads\tic-tac-toe-svgrepo-com.svg"))
        self.setGeometry(675,275,512,512)

        self.label1=QLabel("Welcome to Tic-tac-toe")
        self.label2=QLabel("Player X's Turn")
        self.label1.setStyleSheet("font-size: 27px;""font-family: Nebula;")
        self.label2.setStyleSheet("font-size: 25px;""font-family: Nebula;")
        self.label1.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.label2.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)

        main_layout=QVBoxLayout()
        vbox=QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)
        vbox.setSpacing(5)

        grid_layout=QGridLayout()
        for row in range(3):
            for column in range(3):
                button=self.buttons[row][column]
                button.setFixedSize(150,150)
                grid_layout.addWidget(button,row,column)
        grid_layout.setHorizontalSpacing(5)
        grid_layout.setVerticalSpacing(10)

        main_layout.addLayout(vbox)
        main_layout.addLayout(grid_layout)
        main_layout.setSpacing(15)

        self.setLayout(main_layout)
        self.setStyleSheet("""
            QPushButton{
                font-size: 75px;
                font-family: Arial;
                background-color: black;
                color: #39FF14;
                border: 3px solid black;
                border-radius: 15px;
            }""")
    
    def TTT_backend(self,row,column):
        self.label1.setText("Game on!")
        self.player = "X" if (self.i)%2==0 else "O"

        if self.buttons[row][column].text()==' ':
            nextplayer="X" if (self.i)%2!=0 else "O"
            self.label2.setText(f"It's {nextplayer}'s Turn")
            self.buttons[row][column].setText(self.player)
            self.row_count[self.player][row]+=1
            self.column_count[self.player][column]+=1
            if row==column:
                self.diagonal_count[self.player][0]+=1
            if row+column==2:
                self.antidiagonal_count[self.player][0]+=1
            self.i+=1
        else:
            self.label2.setText("you cannot make that move")

        if 3 in self.row_count[self.player] or 3 in self.column_count[self.player] or 3 in self.diagonal_count[self.player] or 3 in self.antidiagonal_count[self.player]:
            self.label1.setText("Game Over!")
            self.label2.setText(f"{self.player} is the winner")
            self.setEnabled(False)
        if self.i==9:
            self.label1.setText("Game Over!")
            self.label2.setText("It's a Draw!")
            self.setEnabled(False)

    def functionality(self):
        for row in range(3):
            for column in range(3):
                button=self.buttons[row][column]
                button.clicked.connect(lambda _, r=row, c=column:self.TTT_backend(r,c))

if __name__=="__main__":
    app=QApplication(sys.argv)
    TicTacToeMain=TicTacToeWindow()
    TicTacToeMain.show()
    sys.exit(app.exec_())