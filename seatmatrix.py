import sqlite3

class SeatMatrix:
    def __init__(self,s):
        self.s=s

    def display_seat_matrix(self):
        seat_list=s.split(".")

        counter=0
        for seat in seat_list:
            if(counter%10==0):
                print("")
            print(seat,end="  ")
            counter+=1
        booked=0   

        for i in seat_list:
            if i=="*":
                booked+=1       

        available=50-booked
        
        print(f"\nAvailable seats : {available}\nBooked Seats : {booked}\n")
        print("Price per ticket ₹200 ")
        # print(seat_list)
        seat_count=int(input("How many seats do you want to book?\n"))
        dummy=set()
        if seat_count>available:
            print(f"You can only select upto {available} seats\n")
        elif seat_count==0:
            print("Are you kidding me!\n")
            exit()
        else:
            print("Enter seat numbers you want to select:\n")
            tmp=seat_count
            ss=[]
            
            while tmp!=0:
                c=int(input("Enter the seat number:\n"))
                str_c=str(c)
                if(len(str_c)==1):
                    str_c="0"+str_c

                if c<=0 or c>50:
                    print("Invalid seat number. Please enter a valid seat number\n")

                
                elif str(str_c) not in seat_list:
                    print("Seat already taken, please enter a valid seat number:\n")
                elif c not in dummy:
                    ss.append(c)
                    tmp-=1
                    dummy.add(c)
                else :
                    print("Seat is already in your list")
            print("Your selected seats are:",ss)
        
        print("Here is your Booking Reciept:\n")
        print(f"NO_OF_TICKETS: {seat_count}\n")
        print(f"PRICE : ₹{seat_count*200}\n")
        print(f"TAX AMOUNT: ₹{36*seat_count}\n")
        print(f"TOTAL AMOUNT TO BE PAID: ₹{(seat_count*200)+(36*seat_count)}")
        flg=False

        while flg==False:
            c=input("Proceed to payment(Y|N)\n")
            if c=="Y" or c=="y":
                print()
                flg=True
            elif c=="N" or c=="n":
                flg=True
                print("Faltu humara time waste kiya\n")
                exit()
            else :
                print("Invalid response please try again\n")
        return ((seat_count*200)+(36*seat_count))
                


s="01.02.03.04.05.06.07.08.*.10.11.12.13.14.15.*.17.18.19.20.21.22.23.24.*.26.27.28.29.*.31.32.33.34.35.*.37.38.39.40.*.42.43.44.*.46.47.48.*.50"
# a=SeatMatrix(s)
# a.display_seat_matrix()



def Seatmatrix_object(s):
    return SeatMatrix(s)

