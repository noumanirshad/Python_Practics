class Vector:

    def __init__(self, vec):
        self.vec = vec
    
    def __str__(self):
        f = ''
        index = 0
        for i in (self.vec):
            f += f'{i}a{index} '
            index += 1
        return(f)

    def __add__(self, vec2):
        r = []
        for i in range(len(self.vec)):
            r.append(self.vec[i] + vec2.vec[i])
        return Vector(r)

c = Vector([3, 4, 5])
c2 = Vector([4, 6, 7])
print(c)
print(c + c2)



# list = []
# for i in range(len(a)):
#     list.append(a[i]+b[i])

# print(list)




# a = [2,45,6,[2, 34, 65]]
# for i in a:
#     for j in :
#         print()
