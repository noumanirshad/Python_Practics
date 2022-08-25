class TrainTicketBook:
    Train = "Rajdani Express"
    def __init__(self, nameticket, seats, ticketprice):
        self.nameticket = nameticket
        self.seats = seats
        self.ticketprice = ticketprice
        # print(self.seats)
    def avatrain(self):
                print(f"Seats are available {self.seats}")

    def nametrain(self):
        print(f"The name of train is {self.Train}")
        print(f"Price of ticket is {self.ticketprice}")

    def name(self):
        if (self.seats>0):
            print(f"\t********Your ticket has been booked")
            self.seats = self.seats-1
        else:
            print('\t******Sorry, This train is full please try other train:')

    a = [1,2,3, 4,5]
    i = a[3]

    def cancleticket(self):
        if you == 1:
            cancle = int(input("Enter the seat No: "))
            print(f"Seat No {cancle} has been cancled.")
            self.seats = self.seats + 1
    
            


you = int(input("Will you cancle a ticket: (1 = yes  (2 = No: "))
tra = TrainTicketBook(you , 30, "250")
tra.avatrain()
tra.nametrain()
tra.name()
tra.name()
tra.cancleticket()
tra.avatrain()
