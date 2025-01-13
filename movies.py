import sqlite3

class Movie:

    def __init__(self, movies, movie_duration):
        self.movies = movies
        self.movie_duration = movie_duration
        
    def add_movie(self):
        
        conn = sqlite3.connect('User.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS movie
                (movie_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                movie_name TEXT, 
                movie_duration TEXT)
        ''')

        for movie in self.movies:
            cursor.execute("INSERT INTO movie (movie_name, movie_duration) VALUES (?, ?)", (movie, self.movie_duration))

        conn.commit()
        conn.close()


movies = [
    # Bollywood Movies
    "3 Idiots", "Sholay", "Dilwale Dulhania Le Jayenge", "Zindagi Na Milegi Dobara",
    "Kabhi Khushi Kabhie Gham", "Lagaan", "Taare Zameen Par", "Gully Boy",
    "PK", "Dangal", "Chak De! India", "Queen", "Andhadhun", "Drishyam",
    "Kal Ho Naa Ho", "Black", "Barfi!", "Bajirao Mastani", "Padmaavat",
    "Uri: The Surgical Strike", "Gangs of Wasseypur", "Munna Bhai M.B.B.S.",
    "Sanju", "Kahaani", "Badhaai Ho", "Rang De Basanti", "Koi... Mil Gaya",
    "War", "Raazi", "Dear Zindagi", "Bhool Bhulaiyaa 2", "Jaane Bhi Do Yaaro",

    # Hollywood Movies
    "The Shawshank Redemption", "The Godfather", "Inception", "Titanic",
    "Avatar", "The Dark Knight", "The Lion King", "Interstellar", 
    "Pulp Fiction", "Fight Club", "The Matrix", "Forrest Gump", 
    "Avengers: Endgame", "The Avengers", "Joker", "The Wolf of Wall Street",
    "Gladiator", "The Prestige", "The Social Network", "The Grand Budapest Hotel",
    "Gone Girl", "Inglourious Basterds", "The Silence of the Lambs", 
    "Saving Private Ryan", "Schindler's List", "Goodfellas", "Se7en",
    "The Departed", "Braveheart", "The Truman Show", "The Green Mile",

    # Tollywood Movies
    "RRR", "Baahubali: The Beginning", "Baahubali: The Conclusion",
    "Pushpa: The Rise", "Arjun Reddy", "Geetha Govindam", "Ala Vaikunthapurramuloo",
    "Magadheera", "Eega", "Mahanati", "Gabbar Singh", "Sarileru Neekevvaru",
    "Srimanthudu", "Bharat Ane Nenu", "Athadu", "Julayi", "Fidaa",
    "Temper", "Yevadu", "Dookudu", "Legend", "Businessman", "Arya",
    "Arya 2", "Chhatrapati", "Manam", "Oopiri", "Rangasthalam",
    "Kshanam", "Nannaku Prematho", "Vedam", "Jersey", "Bheeshma"
]
a=Movie(movies,"2")
a.add_movie()
print(movies)
