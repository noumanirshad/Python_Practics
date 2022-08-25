class Complex():

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, c):
        f = f"{self.x + c.x}i + {self.y + c.y}j + {self.z + c.z}k"
        print(f)

    def __mul__(self, c):
        f = (self.x * c.x) - (self.y*c.y)
        f2 = (self.x * c.y) + (self.y*c.x)
        c = f"{f}i + {f2}j "
        print(c)
        print(f + f2) 

com = Complex(3, 5, 4)
com2 = Complex(8, 3, 4 )
com + com2
# com * com2

