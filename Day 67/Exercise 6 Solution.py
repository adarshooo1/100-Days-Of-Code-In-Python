# Library Management System

class Library:
    def __init__(self):
        self.noOfBooks = 0
        self.books = []

    def addBook(self , book):
        self.books.append(book)
        self.noOfBooks = len(self.books)


    def showBooks(self):
        print(f"The books in the Library are {self.books} books and total number of books is {self.noOfBooks}")    

library = Library()
library.addBook("Hindi")
library.addBook("English")
library.showBooks()

