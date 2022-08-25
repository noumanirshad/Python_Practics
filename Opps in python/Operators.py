# (ac−bd) + (ad+bc)i
class   Complex:
    def __init__(self,r, i):
        self.real = r
        self.imagniry = i

    def __add__(self, num):
        reel = self.real + num.real 
        img = self.imagniry + num.imagniry
        return (reel,img)
        # return (f"{real} + {img}i")

    def __mul__(self, num):
        reel = (self.real * num.real) - (self.imagniry*num.imaginary)  
        img = (self.real * num.imagniry) + (self.imagniry*num.real)
        return (reel, img)

    def __str__(self):
        return (f"{reel} + {img}i")



v = complex(8, 3)
v1 = complex(3, 4)
print(v + v1)
print(v * v1)