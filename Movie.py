import sqlite3

class Movie:

    # Initialise class
    def __init__(self, movies, movie_duration):
        self.movies = movies
        self.movie_duration = movie_duration
    
    # Admin functions
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

    def remove_movie(self):
        rem_movie=input("Enter movie name to be removed:\n") #admin 

        conn = sqlite3.connect('User.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM movie WHERE movie_name LIKE ? COLLATE NOCASE;\n", (rem_movie,))
        cursor.execute("SELECT movie_name FROM movie")
        movie_list = cursor.fetchall()
        print("Movie removed\n",movie_list)
        conn.commit()
        conn.close()

    # User functions
    def display_movie(self):
        conn = sqlite3.connect('User.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM movie")
        movie_list = cursor.fetchall()

        Flg=False

        while Flg==False:
            movies_dict = {i + 1: movie[1] for i, movie in enumerate(movie_list)}
            print("Select your movie, we are currently showing:\n",movies_dict)
            m=int(input("\nEnter the movie number\n"))
            
            if m>len(movies_dict):
                print("Enter a valid choice")
            else :
                print()
                Flg=True
        conn.close()
      
# Main   
#movies = ["Gully Boy","Dangal", "Queen", "Inception", "Titanic","Avatar", "RRR", "Pushpa: The Rise", "Arjun Reddy"]

#a=Movie(movies,"2")
# a.add_movie() #Admin function
#a.remove_movie() #Admin function
#a.display_movie()



def Movie_object(movies,movie_duration):
    return Movie(movies,movie_duration)



