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
    for entry in data:
        print("Title:", entry['title'])
        print("Genre:", entry['genre'])
        print("Writer:", ", ".join(entry['writer']))
        print()
    print_dictionary(data)

userinput = input("Enter print:")
userinput.lower() == "print:" 