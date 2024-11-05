# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name;
#         self.age = age;
#         self.grade = grade;
    
# student_1 = Student("Asif Hussain",23,100);
# print("My name is : " +student_1.name);
# print("Age is :" + str( student_1.age));
# print("Grade is : " + str(student_1.grade));

# =============task no 01 low level================= 
# Task: Create a simple Book class.

# Define a Book class with the following attributes:

# title (string)
# author (string)
# pages (integer)
# Include an __init__ method to initialize these attributes.

# Add a describe() method that prints the book’s title, author, and page count in a nicely formatted string.

# Create a couple of Book instances and call describe() to test your class.



# solution 
# class Book:
#     def __init__(self, title, author, pages):
#      self.title = title;
#      self.author = author;
#      self.pages = pages;

#     def describe(self):
#         print("Title of Book" + self.title);
#         print("Author : " + self.author);
#         print("Pages : " + str( self.pages))

# book_1 = Book("Quran","Allah",604)
# book_1.describe();



# =============task no 02 intermidate level================= Task:
#  Create a Library class that manages a collection of books.
# Define a Library class with an attribute books, 
# which should be a list to store multiple Book objects.

# Add methods to:

# add_book(book): Adds a book to the library.
# remove_book(book_title): Removes a book by its title.
# list_books(): Prints a list of all books in the library 
# with their title and author.
# Implement an __str__() method for Library to return a 
# summary of the library’s total number of books.

# Test the Library class by creating a few Book instances,
#  adding/removing them from the library, and listing all books

# # solution 
# class Book:
#     def __init__(self,title,author):
#         self.title = title
#         self.author = author

#     def __str__(self):
#         return f"{self.title} written by {self.author}";

# class Library:
#     def __init__(self):
#         self.books = [];
    

#     def add_book(self,book):
#         self.books.append(book);
#         print("Book added successfully");

#     def remove_book(self,book_title):
#         for book in self.books:
#          if book.title ==book_title:
#           self.books.remove(book);
#           print("Book removed successfully");

#     def Show_list(self):
#         for book in self.books:
#             print(book);

# mylibrary = Library()  ;
    
# book1 = Book("Urdu","Asif Hussain");
# book2 = Book("English","Ahmad");
# book3 = Book("Islamiyat","Rasool");

# mylibrary.add_book(book1);
# mylibrary.add_book(book2);
# mylibrary.add_book(book3);

# print("---------Books details---------- ")
# mylibrary.Show_list();

# mylibrary.remove_book('Urdu');
# print("after removing books ")
# mylibrary.Show_list();
  


