def Ref(sum):
    if (sum == 1) or (sum == 0):
        return(1)
    return sum + Ref(sum -1)
a = Ref(10)
print(a)

