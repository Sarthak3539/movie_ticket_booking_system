import sqlite3

class User:
    # Initialize class
    def __init__(self, name, email, phone_number, password): 
        self.name = name
        self.email = email
        self.password = password
        self.phone_number = phone_number
    
    # Add user to the database
    def add_user(self): 
        conn = sqlite3.connect('User.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS user (
            user_id TEXT PRIMARY KEY DEFAULT (hex(randomblob(16))),
            email TEXT UNIQUE, 
            name TEXT,
            phone_number INTEGER,
            password TEXT)
        ''')
        cursor.execute(
            "INSERT INTO user (email, name, phone_number, password) VALUES (?, ?, ?, ?)", 
            (self.email, self.name, self.phone_number, self.password)
        )
        conn.commit()
        conn.close()

class Login:
    # Initialize class
    def __init__(self, email, cur_pass,user_details): 
        self.email = email
        self.cur_pass = cur_pass
        self.user_details=user_details

    # Login function
    def login(self): 
        conn = sqlite3.connect('User.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user WHERE email=?", (self.email,))
        user = cursor.fetchone()  

        if user:  
            actual_pass = user[4]  
            if actual_pass == self.cur_pass:
                self.user_details = {
                    'email': user[1],
                    'name': user[2],
                    'phone_number': user[3]
                }
                print("Login Successful\n")
                return self.user_details
            else:
                print("Invalid Credentials\n")
        else:
            print("User not found\n")

        conn.close()
        

# Main
# # Adding a new user
# a = User("Sarthak", "sarthak@gmail.com", 9876543210, "1234")
# a.add_user()

# Logging in
# a = Login("sarthak@gmail.com", "1234",{})
# a.login()


def User_object(name, email, phone_number ,password):
    return User(name, email, phone_number ,password)

def Login_object(email,cur_pass,user_details):
    return Login(email,cur_pass,user_details)

