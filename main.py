from library import Library

library = Library()

# Add students
library.add_student("S001", "Alice")
library.add_student("S002", "Bob")

# Add books
library.add_book("B001", "Python Basics", "John Doe")
library.add_book("B002", "Data Structures", "Jane Smith")
library.add_book("B003", "Algorithms", "Alan Turing")

# Issue and return
library.issue_book("S001", "B001")
library.issue_book("S002", "B002")
library.list_books()
library.return_book("S001", "B001")
library.list_books()

# Search books
library.search_books("Python")
