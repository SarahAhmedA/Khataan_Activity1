class LibraryBook:
    total_books = 0   # counter: ilang libro na ang nagawa

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        LibraryBook.total_books += 1   # tataas tuwing may bagong libro

    def borrow(self):
        if self.is_borrowed:
            print(f'"{self.title}" ay hiram na.')
        else:
            self.is_borrowed = True
            print(f'You borrowed "{self.title}".')

    def return_book(self):
        if not self.is_borrowed:
            print(f'"{self.title}" has not been borrowed yet.')
        else:
            self.is_borrowed = False
            print(f'Has been restored "{self.title}".')

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} [{status}]"

    def __repr__(self):
        return f"LibraryBook('{self.title}', '{self.author}')"


b1 = LibraryBook("Pride and Prejudice", "JJane Austen")
b2 = LibraryBook("1984 ", "George Orwell")
b3 = LibraryBook("To Kill a Mockingbird", "Harper Lee")

print("Total books:", LibraryBook.total_books)
print(b1)
b1.borrow()
b1.borrow()          
print(b1)
b1.return_book()
b1.return_book()     
print(b1)
print(repr(b2))
print([b1, b2, b3])