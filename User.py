from Book import Book

class User:

    def __init__(self, username:str, password:str):

        self.books = []

        self.username = username
        self.password = password
        self.book_list_id = 'userbooklists/' + username

        # try to find the user's book file, parse it, and add the books
        # to the list. if not possible, create a new empty file with an
        # appropriate username.
        try:
            book_file = open(self.book_list_id, 'r')
            for line in book_file:
                vals = line.split(',')
                new_book = Book(vals[0], vals[1], vals[2])
                self.books.append(new_book)
        except FileNotFoundError:
            book_file = open(self.book_list_id, 'x')
                

    def __str__(self):
        return self.username

    def save_books(self) -> None:
        file_of_books = open(self.book_list_id, 'w')
        entry = ''

        for book in self.books:
            entry = entry + book.title + ',' + book.author + ',' + str(book.year) + ',\n'
        
        file_of_books.write(entry)