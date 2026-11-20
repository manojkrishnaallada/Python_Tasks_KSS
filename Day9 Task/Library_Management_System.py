"""A library stores information about books and digital books. Create a base class Book 
with a constructor to initialize book details. Create a derived class EBook that adds file 
size information. """

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print("Title:", self.title, "| Author:", self.author)

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)             # Book handles title and author
        self.file_size = file_size                  # only EBook has file size

    def display(self):
        super().display()                           # print Book's details first
        print("File size:", self.file_size, "MB")

ebook = EBook("Python Basics", "A. Kumar", 5)
ebook.display()
