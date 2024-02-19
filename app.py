class Library:
    def __init__(self):
        self.file = open('books.txt', 'a+')
        print("""██╗     ██╗██████╗ ██████╗  █████╗ ██████╗ ██╗   ██╗
██║     ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝
██║     ██║██████╔╝██████╔╝███████║██████╔╝ ╚████╔╝ 
██║     ██║██╔══██╗██╔══██╗██╔══██║██╔══██╗  ╚██╔╝  
███████╗██║██████╔╝██║  ██║██║  ██║██║  ██║   ██║   
╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
                                                    """)

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        book_list = self.file.read().splitlines()

        if len(book_list) == 0:
            print('No books found')
        else:
            print('Books found:')

        for book in book_list:
            title, author = book.split(',')[:2]

            print(f"Title: {title} - Author: {author}")

    def add_book(self):
        info_dict = {'title': input('Enter book title: '), 'author': input('Enter book author: '),
                     'release_year': input('Enter first release year: '),
                     'num_of_pages': input('Enter number of pages: ')}

        infos = ','.join(info_dict.values())
        infos += '\n'

        self.file.write(infos)

    def remove_book(self):
        self.file.seek(0)
        book_list = self.file.read().splitlines()

        if len(book_list) == 0:
            print('No books exist')
            return

        info_dict = {'title': input('Enter book title: ')}

        found_books = []
        cursor_places = []
        cursor_place = 0

        for book in book_list:
            title = book.split(',')[0]

            if title == info_dict['title']:
                found_books.append(book)
                cursor_places.append(cursor_place+1)

            cursor_place += 1

        if len(found_books) == 0:
            print('No books found')
            return

        if len(found_books) == 1:
            title, author = found_books[0].split(',')[:2]
            book_list.remove(found_books[0])
            with open('books.txt', 'w') as temp_file:
                for book in book_list:
                    temp_file.write(book)
                    temp_file.write('\n')
            print(f"Book with Title: {title} - Author: {author} deleted successfully")

        # TODO add multiple case


if __name__ == '__main__':
    lib = Library()

    print("""***MENU***
1) List Books
2) Add Book
3) Remove Book
q) Quit""")
    while True:
        selection = input('\nEnter your selection: ')

        if selection == 'q':
            print('HAVE A NICE DAY!')
            break
        elif selection == '1':
            lib.list_books()
        elif selection == '2':
            lib.add_book()
        elif selection == '3':
            lib.remove_book()
        else:
            print('Invalid selection!')

    del lib
