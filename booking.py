import sqlite3

class Booking:

    def __init__(self, user_id, movie_details_id, seat_booked):
        self.user_id = user_id
        self.movie_details_id = movie_details_id
        self.seat_booked = seat_booked
        
    def display_booking(self):
        
        conn = sqlite3.connect('User.db')
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute('''CREATE TABLE IF NOT EXISTS booking(
                booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER, 
                movie_details_id INTEGER, 
                seat_booked TEXT,
                FOREIGN KEY (user_id) REFERENCES user(user_id))
        ''')
        cursor.execute("INSERT INTO booking (user_id, movie_details_id, seat_booked) VALUES (?, ?, ?)", (self.user_id, self.movie_details_id, self.seat_booked))

        conn.commit()
        conn.close()

a=Booking("DCE4FD4F096AE261F59347B1BD28C074",1,"5.6")
a.display_booking()