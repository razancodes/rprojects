#composition in python:
'''
class close:
    class engine:
        def __init__(self,HP):
            self.HP=HP
        def displayengine(self):
            print(f"the engine horsepower is {self.HP}")


    class car:
        def __init__(self,model,hp):
            self.model=model
            self.engine1='y'
        
        def start(self):
            print(f"This is the {self.model} with engine HP of {self.engine1.HP}.")

    car1=car("FORD F150", 768)
    car1.start()
    print(isinstance(car1,car))
    #THERE IS NO WAY TO ACCESS THE 768 HP ENGINE CREATED WHILE THE CAR OBJECT WAS
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

library = Library()
library.add_book(book1)
library.add_book(book2)

print("Books in the library:")
library.list_books()

# Books can still exist without the library
print("\nIndependent Book:")
print(book1)

'''
print("muaz is gay")