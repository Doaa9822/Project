

from BusInfo import *

class admin:
    ins_name = input("Enter your Name")

    buses: [bus1, bus2, bus3]
    def displaybuses(self, buses):
        for i in range(len(buses)):
            print("bus number", BusInfo.getnumber)
            print("bus distination", BusInfo.getdestination)
            print("bus ticket", BusInfo.getprice)
            print("avaiable seats", BusInfo.getseats)


    seatNoList = [1, 2, 3, 4, 5]
    def bookseat(self, seats):
        self.bookingList = []
        while True:
            self.seatNo = int(input("choose a seat number: "))
            if self.seatNo <= 5:

                if self.seatNo in seatNoList:
                    self.bookingList.append(self.seatNo)
                    count = len(seatNoList)
                else:
                    print("ticket already booked!!")
                    w = input("Do you want to book one more seat Y/N?")
                    if w == "Y":
                        pass
                    else:
                        break
            else:
                print("Don't choose a seat number which is not availabe")
                Menu()


def Menu():
    print(""""************************
     **********Menu**************
     1. Display all Buses
     2. Display available seat
     3. Book a free seat """)
global choice
choice = int(input("Enter your choice:"))



while (True):
    if (choice == 1):
        displaybuses()
        print("Do you want to Quit Y/N?")
        if ("Y"):
            break
        else:
            Menu()
    elif (choice == 2):
        displayavailableseat()
        print("Do you want to Quit Y/N?")
        if ("Y"):
            break
        else:
            Menu()
    elif (choice == 3):
        bookseat()
        print("Do you want to Quit Y/N?")
        if ("Y"):
           break
        else:
           Menu()



def Menu():
    return None