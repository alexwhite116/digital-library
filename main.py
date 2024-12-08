import sys
from librarystructures import Library, Book
import csv

def create_book(title: str,
                author: str,
                genre: str,
                pages: int,
                publication_year: int):
    book = Book(title, author, genre, pages, publication_year)
    return book

def get_string_input(prompt: str) -> str:
    user_input = input(prompt)
    if len(user_input) == 0:
        print(prompt[:-2] + ' cannot be empty. Please try again.')
        return get_string_input(prompt)

    return user_input

def get_int_input(prompt: str) -> int:
    try:
        user_input = int(input(prompt))
    except ValueError as e:
        print(f"{e}: Please enter an integer.")
        return get_int_input(prompt)

    return user_input

def main():
    library = Library()
    while True:
        user_input = input("DISPLAY / NEW / EXIT / SAVE: ").lower()

        if user_input == 'exit':
            print('Thank you! Exiting now.')
            sys.exit()

        if user_input == 'display':
            print(library.title_list())
            continue

        if user_input == 'new':
            title = get_string_input("Book Title: ")
            author = get_string_input("Book Author: ")
            genre = get_string_input("Book Genre: ")
            pages = get_int_input("# of Pages: ")
            publication_year = get_int_input("Publication year: ")
            book = create_book(title, author, genre, pages, publication_year)
            library.add_book(book)
            continue

        if user_input == 'save':
            # ...
            continue


        print("Please enter one of the options displayed.")

if __name__ == '__main__':
    main()