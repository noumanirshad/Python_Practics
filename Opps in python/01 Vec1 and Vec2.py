class C2d_vec:
    def __init__(self, i, j):
        self.icap= i
        self.jcap = j

    def __str__(self):
        return(f"{self.icap}i + {self.jcap}j ")



class C3d_vec(C2d_vec):

    def __init__(self, i, j, k):
        super().__init__(i,j)
        self.icap= i
        self.jcap = j
        self.kcap = k

    def __str__(self):
        return(f"{self.icap}i + {self.jcap}j + {self.kcap}k")


vec1 = C2d_vec(4,5)

vec2 = C3d_vec(7,8, 6)
print(vec1)
print(vec2)
