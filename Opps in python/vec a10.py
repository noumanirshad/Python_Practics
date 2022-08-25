class Vector:
    def __init__(self, vec):
        self.vec = vec
        
    def __str__(self):
        a = ""
        index = 0
        for i in self.vec:
            a += (f" {i}a{index} +")
            index += 1
        return a[:-1]

    def __add__(self, vec2):
        list = []
        for i in range(len(self.vec)):
            list.append(self.vec[i] + vec2.vec[i])
        return Vector(list)
    
    def __mul__(self, vec2):
        list = 0
        for i in range(len(self.vec)):
            list += self.vec[i] * vec2.vec[i]
        return(list)

v = Vector([4, 5, 8])
v2 = Vector([6,7,8])
print(v + v2)
print(v * v2)