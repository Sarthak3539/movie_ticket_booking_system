import sqlite3

class Movie_details:

    def __init__(self, movie_id, theatre_id, seat_matrix, ticket_cost):
        
        self.movie_id = movie_id
        self.theatre_id = theatre_id
        self.seat_matrix = seat_matrix
        self.ticket_cost=ticket_cost
        
    def add_movie_detail(self):
        
        conn = sqlite3.connect('User.db')
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute('''CREATE TABLE IF NOT EXISTS movie_details(
                movie_detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
                movie_id INTEGER,
                theatre_id INTEGER, 
                seat_matrix TEXT, 
                ticket_cost INTEGER,
                FOREIGN KEY (movie_id) REFERENCES movie (movie_id),
                FOREIGN KEY (theatre_id) REFERENCES theatre (theatre_id))
        ''')
        cursor.execute("INSERT INTO movie_details ( movie_id, theatre_id, seat_matrix, ticket_cost) VALUES (?, ?, ?, ?)", (self.movie_id, self.theatre_id, self.seat_matrix, self.ticket_cost))

        conn.commit()
        conn.close()

a=Movie_details(1,100,"101",300)
a.add_movie_detail()

