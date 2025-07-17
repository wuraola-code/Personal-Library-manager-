Library = []
def add_book():
    title = input('Enter book title: ')
    author = input('Enter author: ')
    year = input('Enter year of publication: ')
    book ={'title':title, 'author':author, 'year':year,'read':False}
    Library.append(book)
    print(f"'{title}' has been added to your library. \n")

def view_books():
    if not Library:
        print('Library is empty. \n')
        return
    for i, book in enumerate(Library, start=1):
        status = 'read' if book['read'] else 'unread'
        print(f'{book['title']} by{book['author']} ({book['year']})-{status}')

def search_books():    
    query = input('Enter book title to search: ').lower() 
    found = False
    for book in Library:
        if query in book['title'].lower():
            status = 'read' if book['read'] else 'unread'
            print(f' Found: {book['title']} by{book['author']}-{status}')
            found = True
            break
        if not found:
            print('Book not found. \n')

def mark_book():
    view_books()
    if not Library:
        return
    try:
        choice = int(input('Enter book number to mark as read/unread: '))-1
        if 0 <= choice < len(Library):
            Library[choice]['read'] = not Library[choice]['read']
            status = 'Read' if Library[choice]['read'] else 'Unread'
            print(f'Updated:{Library[choice]['title']} is now marked as {status}. \n')
        else:
            print('Invalid book number.\n')
    except ValueError:
        print('Please enter a valid number. \n')

def main():
    while True:
        print('Welcome to Wuraola Personal Library Manager.')
        print('1. Add a new book')
        print('2. View all new book')
        print('3. Search for a book')
        print('4. Mark book as read/unread')
        print('5. Exit\n')
        choice = int (input('Choose an option from (1-5): '))
        if choice == 1:
            add_book()
        elif choice == 2:
            view_books()
        elif choice == 3:
            search_books()
        elif choice == 4:
            mark_book()
        elif choice == 5:
            print('Exiting library manager. Goodbye!')
            break
        else:
            print('Invalid option. Please try again. \n')

main()
