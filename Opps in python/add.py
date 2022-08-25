class Number:
    def __init__(self, num1):
        self.num1 = num1

    def __add__(self, num2):
        self.num2 = num2
        print("Lets add")
        print(self.num2+num2.num1)

    
c = Number(4)
c2 = Number(5)
c + c2