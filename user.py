class Bus:
    def __init__(self,number,route,total_seats, booked_seats):
        self.number=number
        self.route=route
        self.total_seats=total_seats
        self.booked_seats=0

    def available_seats(self):
        unbooked_seats = self.total_seats- self.booked_seats
        return unbooked_seats
    
    def book_seat(self):
        if self.available_seats() >0 :
            self.booked_seats+=1
            return True
        return False
    

class Passenger:
    def __init__(self,name,phone,bus):
        self.name=name
        self.phone=phone
        self.bus=bus

class BusSystem:
    def __init__(self):
        self.bus_list=[]
        self.passenger_list=[]


class Admin:
    def __init__(self, username, password):
        self.username=username
        self.password=password

    def add_bus(self):