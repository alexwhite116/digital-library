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
        print(f"Error: {e} --- Please enter an integer.")
        return get_int_input(prompt)

    return user_input

def get_book_details() -> list[str | int]:
    details: list[str | int] = [get_string_input("Book Title: "),
                                get_string_input("Book Author: "),
                                get_string_input("Book Genre: "),
                                get_int_input("# of Pages: "),
                                get_int_input("Publication year: ")]
    return details

def save_library(filename: str, library: Library) -> None:
    if filename[-4:] == '.csv':
        filename = filename[:-4]
    libraryList: list[dict] = [book.to_dict() for book in library.books]
    print('Saving...')
    with open(f'{filename}.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=libraryList[0].keys())
        writer.writeheader()
        writer.writerows(libraryList)
    print(f'Saved successfully to {filename}.csv')

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
            # details = get_book_details()
            details = ['Great Expectations', 'Charles Dickens', 'Classical Fiction', 479, 1861]
            book = create_book(*details) # unpack details
            library.add_book(book)
            continue

        if user_input == 'save':
            save_library('books', library)
            continue


        print("Please enter one of the options displayed.")

if __name__ == '__main__':
    main()