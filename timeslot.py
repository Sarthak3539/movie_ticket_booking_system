import sqlite3
from datetime import datetime,timedelta

class DateTime:

    # Initialise class
    def __init__(self,start_time,end_time):
        self.start_time=start_time
        self.end_time=end_time


    def add_time_slot(self):
        conn = sqlite3.connect('User.db')
        cursor = conn.cursor()
        conn.close()

    def display_date(self):
        current_day=datetime.now()
        tomorrow=current_day+timedelta(1)
        day_after_tomorrow=current_day+timedelta(2)
        current_month = current_day.strftime("%B")
        tomorrow_month= tomorrow.strftime("%B")
        day_after_tomorrow_month=day_after_tomorrow.strftime("%B")

        # print(current_day)
        # print(current_month)
        flg=False

        while flg==False:
                
            print("Select day of movie:\n")

            print(f"1.{current_day}-{current_month}")
            print(f"2.{tomorrow}-{tomorrow_month}")
            print(f"3.{day_after_tomorrow}-{day_after_tomorrow_month}")
            c=int(input("Select the date:\n"))


            if c>3:
                print("Enter a valid choice/n")
            else :
                print("Redirect to next page/n")
                flg=True

        #select timeslot  
        time_list_admin=[10,13,16,19,21]
        time_list_user=["10:00am-12:00pm","1:00pm-3:00pm","4:00pm-6:00pm","7:00pm-9:00pm","9:00pm-11:00pm"]
        current_hour=current_day.hour
        print("Select your timeslot:\n")
        for i in range(0,5):
            if c==1 and time_list_admin[i]<=current_hour:
                continue
            print(f"{i+1}.{time_list_user[i]}")

            
                    
a=DateTime("2","4")
a.display_date()