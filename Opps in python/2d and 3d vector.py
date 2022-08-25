# class C2dVector():
    
#     def __init__(self, i, j):
#         self.icap = i
#         self.jcap = j
#         print(f"{self.icap}i + {self.jcap}j")

# class C3dVector(C2dVector):
#     def __init__(self, i , j , k):
#         super().__init__(i,j)
#         self.kcap = k
#         print(f"{self.icap}i + {self.jcap}j + {self.kcap}k")

# v1 = C2dVector(4, 6)
# v3 = C3dVector(33, 36, 9)

class C2dVector():

    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return(f"{self.icap}i + {self.jcap}j")

class C3dVector(C2dVector):
    def __init__(self, i , j , k):
        super().__init__(i,j)
        self.kcap = k
    def __str__(self):
        return(f"{self.icap}i + {self.jcap}j + {self.kcap}k")

v1 = C2dVector(4, 6)
v3 = C3dVector(33, 36, 9)
print(v1)
print(v3)