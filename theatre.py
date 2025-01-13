import sqlite3

class Theatre:

    def __init__(self, theatre_name, theatre_location, theatre_city):
        self.theatre_name = theatre_name
        self.theatre_location = theatre_location
        self.theatre_city = theatre_city
        
    def add_theatre(self):
        
        conn = sqlite3.connect('User.db')
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")

        cursor.execute('''CREATE TABLE IF NOT EXISTS theatre
                (theatre_id INTEGER PRIMARY KEY AUTOINCREMENT,
                theatre_name TEXT,
                theatre_location TEXT, 
                theatre_city TEXT,
                FOREIGN KEY (theatre_city) REFERENCES city(city_name))
''')
                           
        cursor.execute("INSERT INTO theatre (theatre_name, theatre_location, theatre_city) VALUES (?, ?, ?)", (self.theatre_name, self.theatre_location, self.theatre_city))

        conn.commit()

a=Theatre("pvr","bkc","jljglkdfjg")
a.add_theatre()