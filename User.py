import sqlite3

class User:

    def __init__(self, name, email, phone_number ,password):
        self.name = name
        self.email = email
        self.password = password
        self.phone_number = phone_number
        
    def add_user(self):
        
        conn = sqlite3.connect('User.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS user(
            user_id TEXT PRIMARY KEY DEFAULT (hex(randomblob(16))),
            email TEXT UNIQUE, 
            name TEXT,
            phone_number INTEGER,
            password TEXT)
        ''')
        cursor.execute("INSERT INTO user (email, name, phone_number, password) VALUES (?, ?, ?, ?)", (self.email,self.name,self.phone_number,self.password))

        conn.commit()
        conn.close()

class Login:
    def __init__(self,email,cur_pass):
        self.email=email
        self.cur_pass=cur_pass

    def login(self):
        conn = sqlite3.connect('User.db')
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM User WHERE email=?",(self.email,))
        actual_pass=cursor.fetchone()
        if actual_pass[0]==self.cur_pass:
            print("Login Sucessful")
        else :
            print("Invalid Credentials")

    def display_user_info():
        print("details are showed below:")
        

a=User("gazal","fljs",434,"42z#342")
a.add_user()

# a=Login("fljs",'42z#342')
# a.login()
