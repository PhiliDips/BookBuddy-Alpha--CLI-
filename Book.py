class Book:
    
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return self.title + ' by ' + self.author + ' (' + str(self.year) + ')'