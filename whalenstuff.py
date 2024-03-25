import datetime
today = datetime.date.today()
year = today.year
class Movie():
    def ___init__(self,title,year,genre):
        self.title = title
        self.year = year
        self.genre = genre
    #_str_function that runs when we print or refer to the new
    def __str__(self):
        return f"{self.title}, {self.year}"
    def how_old(self):
        return year - self.year



Star_Wars = Movie("Star Wars", 1977, ['Sci-Fi'])
Avengers = Movie("Avengers", 2014, ['Comic'])
print(Avengers.how_old())