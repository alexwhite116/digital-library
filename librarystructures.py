class Book:
    def __init__(self,
                 title: str,
                 author: str,
                 genre: str,
                 pages: int,
                 publication_year: int):
        self.title: str = title
        self.author: str = author
        self.genre: str = genre
        self.pages: int = pages
        self.publication_year: int = publication_year


    def to_dict(self) -> dict[str, str | int]:
        book_dictionary = {
            'title' : self.title,
            'author' : self.author,
            'genre' : self.genre,
            'pages' : self.pages,
            'publication_year' : self.publication_year
        }
        return book_dictionary

    def to_list(self) -> list[str | int | None]:
        book_list = [
            self.title,
            self.author,
            self.genre,
            self.pages,
            self.publication_year
        ]
        return book_list

    def dict_to_book(self, dictionary: dict[str, str | int]):
        try:
            self.title = dictionary['title']
            self.author = dictionary['author']
            self.genre = dictionary['genre']
            self.pages = dictionary['pages']
            self.publication_year = dictionary['publication_year']
        except KeyError as e:
            print(f'{e} --- Dictionary should have keys: "title", "author", "genre", "pages", "publication_year"')

class Library:
    def __init__(self):
        self.books: list[Book] = []

    def title_list(self) -> str:
        titles = ''

        if not self.books: # self.books is empty
            return 'There are no books currently stored in the library'

        for i, book in enumerate(self.books):
            titles += f"{i}: {book.title}\n"
        return titles

    def add_book(self, book: Book):
        self.books.append(book)