book_list = [ {
    'title': "Pride and Punishment",
    'genre': "romance",
    'writer': ["Jane Austen, Anna Quindlen"]
}, { 

    'title': "Crime and Punishment",
    'genre': "philosophy",
    'writer': ["Fyodor Dostoevsky"]
}, {
    'title': "Hamlet",
    'genre': "drama",
    'writer': ["William Shakespeare"]
}]
book_name = input("Input your books:") 
def print_dictionary(data, book_name):
    for book in book_list:
        if 'title'.lower() == book_name.lower():
            print(f"Title:{book['title']}")
            print(f"Genre:{book['genre']}")
        for writer in book['writer']:
            print(f"Writer:{book['writer']}")
        else:
            print("Book not found")
    print_dictionary(data, book_name)


