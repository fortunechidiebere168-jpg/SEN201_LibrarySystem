class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.issued_books = []

    def issue_book(self, book):
        self.issued_books.append(book)

    def return_book(self, book):
        if book in self.issued_books:
            self.issued_books.remove(book)

    def __str__(self):
        books = ', '.join([book.title for book in self.issued_books]) or "No books issued"
        return f"{self.student_id} - {self.name} | Books: {books}"
