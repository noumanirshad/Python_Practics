class Number:
    def squareCubeSquareRoot(self, num):
        self.num = num
        print(f"Square of {self.num} is {self.num**2}\nSquareRoot of {self.num} is {self.num**0.5}\nCube of {self.num} is {self.num**3}")
f = int(input("Enter the number: "))
a = Number()
a.squareCubeSquareRoot(f)

