import sys
from librarystructures import Library, Book
import csv
import os

def create_book(title: str,
                author: str,
                genre: str,
                pages: int,
                publication_year: int):
    book = Book(title, author, genre, pages, publication_year)
    return book

def get_string_input(prompt: str) -> str:
    user_input: str = input(prompt)
    if len(user_input) == 0:
        print(prompt[:-2] + ' cannot be empty. Please try again.')
        return get_string_input(prompt)

    return user_input

def get_int_input(prompt: str) -> int:
    try:
        user_input: int = int(input(prompt))
    except ValueError as e:
        print(f"Error: {e} --- Please enter an integer.")
        return get_int_input(prompt)

    return user_input

def get_yes_no_input(prompt: str) -> str:
    user_input = input(prompt).lower()
    if len(user_input) != 1:
        print('Type Y/N')
        return get_yes_no_input(prompt)

    if user_input != 'y' and user_input != 'n':
        print('Type Y/N')
        return get_yes_no_input()

    return user_input

def get_book_details() -> list[str | int]:
    details: list[str | int] = [get_string_input("Book Title: "),
                                get_string_input("Book Author: "),
                                get_string_input("Book Genre: "),
                                get_int_input("# of Pages: "),
                                get_int_input("Publication year: ")]
    return details

def save_library(filename: str, library: Library) -> None:
    if filename[-4:] == '.csv': # if user includes .csv extension, remove it
        filename: str = filename[:-4]
    library_list: list[dict] = [book.to_dict() for book in library.books]
    print('Saving...')
    with open(f'{filename}.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=library_list[0].keys())
        writer.writeheader()
        writer.writerows(library_list)
    print(f'Saved successfully to {filename}.csv')

# Get filename, check that it is in 'libraries/' folder, and return if it is
def input_load_file(prompt: str) -> str | bool:
    filename: str = input(prompt)
    if filename[-4:] != '.csv': # if filepath doesn't include .csv, add it
        filename = f'{filename}.csv'

    # check if file name is in 'libraries/'
    if filename not in os.listdir('libraries/'):
        # if file doesn't exist, ask if user wants to try again or give up on load
        abort_choice: str = get_yes_no_input('File name does not exist in "libraries/" folder. Abort load? (Y/N) ')
        # if user wants to try again, recursively call this function
        if abort_choice == 'n':
            return input_load_file(prompt)
        else:
            return False # indicates user has stopped trying to load and the main loop should continue

    return filename

def main():
    library = Library()
    while True:
        print() # blank line
        user_input = input("DISPLAY / NEW / EXIT / SAVE / LOAD / CLEAR: ").lower()

        if user_input == 'exit':
            print('Thank you! Exiting now.')
            sys.exit()

        if user_input == 'display':
            print(library.title_list())
            continue

        if user_input == 'new':
            # details = get_book_details()
            details = ['Great Expectations', 'Charles Dickens', 'Classical Fiction', 479, 1861]
            book: Book = create_book(*details) # unpack details
            library.add_book(book)
            continue


        if user_input == 'save':
            # Create libraries folder if it doesn't exist
            if not os.path.isdir('libraries'):
                os.makedirs('libraries', exist_ok=False) # exist_ok=False, should not overwrite existing folder

            # Get file name from user and save in libraries/filepath
            filepath: str = get_string_input('File name: ')
            filepath = f'libraries/{filepath}'

            # File doesn't exist, save normally
            if not os.path.isfile(f'{filepath}.csv'):
                save_library(filepath, library)
                continue

            # File already exists. Handle whether to overwrite
            print('File already exists.')
            overwrite_choice: str = get_yes_no_input('Do you want to overwrite? (Y/N) ')

            if overwrite_choice == 'y':
                save_library(filepath, library)
                continue
            elif overwrite_choice == 'n':
                print('Save cancelled. Please try again with different file name.')
                continue
            else:
                raise Exception("Inputs should be y/n") # raise exception if unexpected behaviour has occurred


        if user_input == 'load':
            library_files = os.listdir('libraries/')
            print('Available files in "libraries/":')
            for file in library_files:
                print(f"-{file}")

            file_to_load: str | bool = input_load_file('Enter the file above you want to load: ')
            if not file_to_load: # if user has given up on loading, then continue loop
                continue

            print(f'Loading from libraries/{file_to_load}...')
            with open(f'libraries/{file_to_load}', newline='\n') as library_file:
                reader = csv.reader(library_file, delimiter=',')
                next(reader)
                for row in reader:
                    book = Book(*row)
                    library.add_book(book)
            print('Library successfully loaded!')
            continue

        if user_input == 'clear':
            library = Library()
            print('Library cleared of all books')
            continue

        print("Please enter one of the options displayed.")

if __name__ == '__main__':
    main()