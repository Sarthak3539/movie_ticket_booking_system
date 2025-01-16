import sqlite3
from datetime import datetime,timedelta
import time

class DateTime:


    def add_time_slot(self):
        conn = sqlite3.connect('User.db')
        cursor = conn.cursor()
        conn.close()

    def display_date(self):
        current_time = datetime.now()
        current_day = current_time.day
        tomorrow=current_time+timedelta(1)
        day_after_tomorrow=current_time+timedelta(2)
        current_month = current_time.strftime("%B")
        tomorrow_month= tomorrow.strftime("%B")
        day_after_tomorrow_month=day_after_tomorrow.strftime("%B")

        # print(current_day)
        # print(current_month)
        flg=False

        while flg==False:
                
            print("\nSelect day of movie:\n")

            print(f"1.{current_day}-{current_month}")
            print(f"2.{tomorrow.day}-{tomorrow_month}")
            print(f"3.{day_after_tomorrow.day}-{day_after_tomorrow_month}")
            c=int(input("Select the date:\n"))


            if c>3:
                print("Enter a valid choice\n")
            else :
                print()
                flg=True

        # select timeslot  
        time_list_admin=[10,13,16,19,21]
        time_list_user=["10:00am-12:00pm","01:00pm-03:00pm","04:00pm-06:00pm","07:00pm-09:00pm","09:00pm-11:00pm"]
        current_hour=current_time.hour
        
        print("Select your timeslot:\n")
        time_slot_dict={}
        j=1
        for i in range(0,5):
            if c==1 and time_list_admin[i]<=current_hour:
                continue
            time_slot_dict[j]=time_list_user[i]
            j+=1
            
        for key,value in time_slot_dict.items():
            print(f"{key}.{value}")
        flg=False
        while flg==False:    
            m=int(input())
            if m not in time_slot_dict.keys():
                print("Enter a valid choice\n")   
            else:
                print()
                flg=True

            
                    
# a=DateTime()
# a.display_date()

def DateTime_object():
    return DateTime()