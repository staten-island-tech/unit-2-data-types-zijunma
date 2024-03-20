book_list = [
     {
    'title': "Pride and Punishment",
    'genre': "Romance",
    'writer': ["Jane Austen, Anna Quindlen"]
    },{
    'title': "Crime and Punishment",
    'genre': "Philosophy",
    'writer': ["Fyodor Dostoevsky"]
    },{
    'title': "Hamlet",
    'genre': "Drama",
    'writer': ["William Shakespeare"]
    }
]
def print_dictionary(book_title, data):
    for entry in data:
        if entry['title'].lower() == book_title.lower():
            print("Title:", entry['title'])
            print("Genre:", entry['genre'])
            print("Writer:", ",".join(entry['writer']))
            return
    print("Book not found")

userinput = input("Enter book title: ")
print_dictionary(userinput, book_list)