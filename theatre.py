import sqlite3

class Theatre:

    # Initialise class
    def __init__(self, theatre_name, theatre_location, theatre_city):
        self.theatre_name = theatre_name
        self.theatre_location = theatre_location
        self.theatre_city = theatre_city

    # Admin functions
    def add_theatre(self):
        
        conn = sqlite3.connect('User.db')
        cursor = conn.cursor()
        #cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute('''CREATE TABLE IF NOT EXISTS theatre
                (theatre_id INTEGER PRIMARY KEY AUTOINCREMENT,
                theatre_name TEXT UNIQUE,
                theatre_location TEXT, 
                theatre_city TEXT,
                FOREIGN KEY (theatre_city) REFERENCES city(city_name))
                ''')
        for x in self.theatre_name:                
            cursor.execute("INSERT INTO theatre (theatre_name, theatre_location, theatre_city) VALUES (?, ?, ?)", (x, self.theatre_location, self.theatre_city))
        cursor.execute("SELECT * FROM theatre")
        theatre_list = cursor.fetchall()
        print(theatre_list)
        conn.commit()
        conn.close()

    def remove_theatre(self):
        rem_theatre=input()
        conn = sqlite3.connect('User.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM theatre WHERE theatre_name LIKE ? COLLATE NOCASE;\n", (rem_theatre,))
        theatre_list = cursor.fetchall()
        print(theatre_list)
        conn.close()

    
    def delete_theatre_table(self):
        conn = sqlite3.connect('User.db')
        cursor = conn.cursor()
        cursor.execute("drop table theatre")

    # User functions
    def display_theatre(self):
        conn = sqlite3.connect('User.db')
        cursor = conn.cursor()

        cursor.execute("SELECT theatre_name FROM theatre")
        theatre_list = cursor.fetchall()

        Flg=False

        while Flg==False:
            theatre_dict = {i + 1: theatre[0] for i, theatre in enumerate(theatre_list)}
            print("Select your theatre\n",theatre_dict)
            m=int(input("Enter the theatre number:\n"))
            
            if m>len(theatre_dict):
                print("Enter a valid choice")
            else :
                print("Redirect to next page")
                Flg=True
        conn.close()

# Main

theatre = ["PVR","INOX", "Cinepolis","IMAX","MovieMax" ]
a=Theatre(theatre,"tmp","tmp")
# a.remove_theatre()
# a.delete_theatre_table()
# a.add_theatre() #Admin function
a.display_theatre()


