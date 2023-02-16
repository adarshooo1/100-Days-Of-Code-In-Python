# Library Management System

class Library:
    #This method will have the count of the books as well as lisy of books.
    def __init__(self):
        self.noOfBooks = 0
        self.books = []

    #This will help to add the books.
    def addBook(self , book):
        self.books.append(book)
        self.noOfBooks = len(self.books)

    #This method will show the details of book in the Library.
    def showBooks(self):
        print(f"The books in the Library are {self.books} books and total number of books is {self.noOfBooks}")    

library = Library()
library.addBook("Hindi")
library.addBook("English")
library.showBooks()

