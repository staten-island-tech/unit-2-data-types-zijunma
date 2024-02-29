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
        print(f"Title:{book['Title']}")
        print(f"Genre:{book['Genre']}")
        print("Writers:")
        for writer in book['Writers']:
            print(f" - {writer}")
        