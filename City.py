import sqlite3
class City:

    # Initialise class
    def __init__(self, city_names): 
        self.city_names = city_names

    # Admin functions
    def add_city(self): 
        conn = sqlite3.connect("User.db")
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS city (
            city_id TEXT PRIMARY KEY DEFAULT (hex(randomblob(16))),
            city_name TEXT NOT NULL
        );
        """)
        for city_name in self.city_names:
            try:
                cursor.execute("INSERT INTO city (city_name) VALUES (?);", (city_name,))
                conn.commit()
            except sqlite3.IntegrityError as e:
                print(f"Could not insert {city_name}: {e}")
        conn.close()

    # User functions
    def display_city(self): 
        print("Enter your city:")
        c=input()
        conn = sqlite3.connect('User.db')
        cursor = conn.cursor()
        result = cursor.execute('''SELECT COUNT(*) FROM city WHERE city_name LIKE ? COLLATE NOCASE;''', (c,))
        count = result.fetchone()[0]  
        if count>0:
            print()
        else:
            print("City is not exist. Please enter a valid city.")
            exit()

# Main
# city_names=[]

# a = City(city_names)
# a.add_city()

# b=City([])
# b.display_city()

def City_object(city_names):
    return City(city_names)
