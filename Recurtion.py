def fec(x):
    if (x == 1 or x == 0):
        return(1) 
    return(x * fec(x-1) )

fc = int(input("Enter the value: "))
a = fec(fc)
print(a)

# def sum(x):
#     if (x == 1):
#         return(1)
#     return(x * sum(x-1))
# re = sum(6)
# print(re)
# print(1+2+3+4+5+6+7+8+9+10)