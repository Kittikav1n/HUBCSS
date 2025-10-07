books = []

def add_book(books, isbn, title, author, copies):
    book ={
        'isbn': isbn, #รหัส
        'title': title, #ชื่อหนังสือ
        'author': author, #ผู้แต่ง
        'total_copies': copies #จำนวน
    }

    if any(b['isbn'] == isbn for b in books):
        print(f"# Book with ISBN {isbn} already exists.")
        return 1
    else:
        books.append(book)
        return books

def search_books(books, keyword):
    results = []
    for book in books:
        if keyword.lower() in book['title'].lower() or keyword.lower() in book['author'].lower():
            results.append(book)
    return results    

#Show all books 
def show_books(books):
    if not books:
        print("No books available.")
    else:
        for book in books:  
            print(f"ISBN:{book['isbn']}, Title: {book['title']}, Author: {book['author']}, Copies: {book['total_copies']}")

def show_search_books(results):
    if not results:
        print("No matching books found.")
    else:
        show_books(results)



add_book(books, '001', 'Python Crash Course', 'Eric Matthes', 3)
add_book(books, '002', 'Clean Code', 'Robert Martin', 2)
add_book(books, '003', 'The Pragmatic Programmer', 'Hunt & Thomas', 2)
add_book(books, '004', 'Design Patterns', 'Gang of Four', 1)
add_book(books, '005', 'Introduction to Algorithms', 'Cormen et al.', 2)
add_book(books, '006', 'Code Complete', 'Steve McConnell', 3)
add_book(books, '007', 'Refactoring', 'Martin Fowler', 2)
add_book(books, '007', 'Refactoring', 'Martin Fowler', 2)

print()
print("All Books")
show_books(books)
print()
print("Add Book")
add_book(books, input("Enter ISBN: "), input("Enter Title: "), input("Enter Author: "), input("Enter Copies: "))

print()
print("All Books")
show_books(books)

print()
print("Search Books")
results = search_books(books, input("Enter a keyword to search: "))
show_search_books(results)
