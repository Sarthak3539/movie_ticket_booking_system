from User import User_object
from User import Login_object
from City import City_object
from Movie import Movie_object
from theatre import Theatre_object
from timeslot import DateTime_object
from seatmatrix import Seatmatrix_object
from payment_window import payment_window
import time

print("\n\n=====================  WELCOME TO BOOK YOUR SHOW  =====================\n\n\n")

user_details={}
flg=False
while flg==False:
    a=int(input("""Enter your choice:
                1.Login
                2.Register\n"""))
    
    flg=False
    
    while flg==False:
        if a==1:
            email=input("Enter your email\n")
            cur_pass=input("Enter your password\n")
            a=Login_object(email,cur_pass,user_details)
            user_details=a.login()
            # print(user_details)
            flg=True

        elif a==2:
            name=input("Enter your name:\n")
            email=input("Enter your email\n")
            ph_no=int(input("Enter your Phone Number\n"))
            password=input("Enter your password\n")

            b=User_object(name,email,ph_no,password)
            b.add_user()

            print("Login to your account:\n")
            email=input("Enter your email\n")
            cur_pass=input("Enter your password\n")
            a=Login_object(email,cur_pass)
            a.login()
            flg=True
        

        else:
            print("Incorrect choice1\n")
    
c=City_object([])
c.display_city()
    
d=Movie_object([],2)
d.display_movie()
        
e=Theatre_object('er','er','er')
e.display_theatre()

f=DateTime_object()
f.display_date()

s="01.02.03.04.05.06.07.08.*.10.11.12.13.14.15.*.17.18.19.20.21.22.23.24.*.26.27.28.29.*.31.32.33.34.35.*.37.38.39.40.*.42.43.44.*.46.47.48.*.50"

g=Seatmatrix_object(s)
payment=g.display_seat_matrix()
payment_window(payment)
    