from book import Book
from student import Student

class Library:
    def __init__(self):
        self.books = []
        self.students = []
        self.issued_books_log = []

    def add_book(self, book_id, title, author):
        book = Book(book_id, title, author)
        self.books.append(book)
        print(f"Book '{title}' added successfully!")

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"Book '{book.title}' removed!")
                return
        print("Book not found!")

    def add_student(self, student_id, name):
        student = Student(student_id, name)
        self.students.append(student)
        print(f"Student '{name}' registered successfully!")

    def issue_book(self, student_id, book_id):
        student = next((s for s in self.students if s.student_id == student_id), None)
        book = next((b for b in self.books if b.book_id == book_id), None)

        if not student:
            print("Student not found!")
            return
        if not book:
            print("Book not found!")
            return
        if book.is_issued:
            print(f"Book '{book.title}' is already issued!")
            return

        book.mark_issued()
        student.issue_book(book)
        self.issued_books_log.append((student, book))
        print(f"Book '{book.title}' issued to '{student.name}'!")

    def return_book(self, student_id, book_id):
        student = next((s for s in self.students if s.student_id == student_id), None)
        book = next((b for b in self.books if b.book_id == book_id), None)

        if not student or not book:
            print("Student or Book not found!")
            return

        book.mark_returned()
        student.return_book(book)
        print(f"Book '{book.title}' returned by '{student.name}'!")

    def search_books(self, keyword):
        found = [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
        if not found:
            print("No books found!")
        for book in found:
            print(book)

    def list_books(self):
        print("Library Books:")
        for book in self.books:
            print(book)
