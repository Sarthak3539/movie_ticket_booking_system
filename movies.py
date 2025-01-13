import sqlite3

class Movie:

    def __init__(self, movie_name, movie_duration):
        self.movie_name = movie_name
        self.movie_duration = movie_duration
        
    def add_movie(self):
        
        conn = sqlite3.connect('User.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS movie
                (movie_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                movie_name TEXT, 
                movie_duration TEXT)
        ''')
        cursor.execute("INSERT INTO movie (movie_name, movie_duration) VALUES (?, ?)", (self.movie_name, self.movie_duration))

        conn.commit()
        conn.close()
a=Movie("avernges","2")
a.add_movie()