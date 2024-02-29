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
def print_dictionary(data):
    for book in data:
        print(f"Title:{book['title']}")
        print(f"Genre:{book['genre']}")
        print("Writers:")    
        for writer in book['writer']:
            print("f - {author}")
            print("\n")
print_dictionary(book_list)