from User import User
from Book import Book

class BookDataBase:


    def __init__(self) -> None:

        self.invalid_passwords = {
        ''
        }

        self.running = True

        self.cmd = ""
        self.users = []
        self.current_user = None


        self.load_users() # populate users[] from users.txt

        print('book data storage Alpha v0.3')
        print('(c) philip harker 2021')
        print('type "help" for a list of commands')
        print('----------------------------------')
        while self.running:
            print('enter a command...')
            cmd = input()

            #quit program
            if cmd == 'quit':
                self.log_out() # to make sure books are saved
                self.running = False
            #command list
            elif cmd == 'help':
                print(self.help_str())
            #login to account
            elif cmd == 'login':
                self.log_in()
            #register new account
            elif cmd == 'register':
                self.register()
            #logout
            elif cmd == 'logout':
                self.log_out()
            #view books
            elif cmd == 'view':
                self.view_books()
            #add books
            elif cmd == 'add':
                self.add_new_book()
            else:
                print('unknown command')

        print('end of program')


    def add_new_book(self) -> None:
        if self.current_user == None:
            print('not logged in') # doing this for each command seems inelegant
        else:
            print('enter book name')
            book_name = input()
            print('enter author')
            book_author = input()

            book_year = 'undef'
            # sentinel loop to ensure year entered is a valid integer
            while book_year.__class__ is not int:
                print('enter year of publication')
                book_year = input()
                try:
                    book_year = int(book_year)
                except ValueError:
                    print('error: invalid year entered')


            new_book = Book(book_name, book_author, book_year)
            self.current_user.books.append(new_book)
            print('added ' + str(new_book) + ' to your list')


    def help_str(self) -> str:
        val = """
        help: list of commands
        quit: quit to OS
        register: create account
        login: log in to account
        ------------------------
        logged in users only:
        logout: log out of account
        view: see all books
        add: add book to listing"""

        return val


    def log_in(self) -> None:
        print('enter username')
        username = input()

        # assume user does not exist, try to find username in list of users
        user_exists = False
        for user in self.users:
            if user.username == username:
                user_exists = True
                print('enter password')
                password = input()
                
                if user.password == password:
                    print('welcome, ', user.username)
                    self.current_user = user
                else:
                    print('incorrect password')
            
        if not user_exists:
            print('user does not exist')


    def log_out(self) -> None:
        if self.current_user is None:
            print('not logged in')
        else:
            self.current_user.save_books()
            self.current_user = None


    def save_users(self) -> None:
        user_data = open('users.txt', 'a')

        user_data.truncate(0) # wipes file to rewrite users (probably bad practice idk)

        for user in self.users:
            user_data.write(user.username + ',' + user.password + ',\n')


    def load_users(self) -> None:
        user_data = open('users.txt')
        
        for line in user_data:
            credentials = line.split(',')
            self.users.append(User(credentials[0], credentials[1]))


    def register(self) -> None:
        print('enter username')
        username = input()
        if self.username_already_taken(username):
            print('"' + username + '" is taken')
            return # user must restart registration process
        print('enter password')
        password = input()
        print('confirm password')
        if password == input() and password not in self.invalid_passwords:
            new_user = User(username, password)
            self.users.append(new_user)
            self.current_user = new_user
            print('welcome, ', self.current_user.username)
            self.save_users() # rewrite user list to include new user
        else:
            print('password invalid or does not match')


    def username_already_taken(self, name:str) -> bool:
        taken = False
        
        for user in self.users:
            if user.username == name:
                taken = True
                break
        return taken


    def view_books(self) -> None:
        if self.current_user == None:
            print('not logged in')
        else:
            print('current books:')
            for book in self.current_user.books:
                print(book)
