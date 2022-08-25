class train:
    seats = 3
    def bookticket(self):
        if(self.seats>0):
            print(f"Your ticked has been booked. Your seat no is {self.seats} ")
            self.seats = self.seats - 1

        else:
            print("Sorry: The Train is full. Please try in latter. ")
    
    # def cancleTicket(self):
            
    def __init__(self, name, fear):
        self.name = name
        self.fear = fear

    def getstatus(self):
        print(f"Name of train is {self.name}\nTotal seats are {self.seats}\nThe price of 1 ticket is {self.fear}")    

    
info = train("Rajdani Express: 1299", 450)
info.getstatus()
info.bookticket ()
info.bookticket ()
info.getstatus()
info.bookticket ()
info.bookticket ()