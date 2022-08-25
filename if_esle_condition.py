n1 = int(input("Enter the number: "))
n2 = int(input("Enter the number: "))
n3 = int(input("Enter the number: "))
n4 = int(input("Enter the number: "))
 
# if (n1>n4):
#     if(n2>n3):
#         if(n1>n2):
#             print(str(n1) + " is the greatest number")
#         else:
#             print(str(n2) + " is the greatest number")
#     else:
#         if(n1>n3):
#             print(str(n1) + " is the greatest number")
#         else:
#             print(str(n3) + " is the greatest number") 
# else:
#     if(n2>n3):
#         if(n4>n2):
#             print(str(n4) + " is the greatest number")
#         else:
#             print(str(n2) + " is the greatest number")
#     else:
#         if(n4>n3):
#             print(str(n4) + " is the greatest number")
#         else:
#             print(str(n3) + " is the greatest number")

if(n1>n4):
    f1 = n1
else:
    f1 = n4

if(n2>n3):
    f2 = n2
else:
    f2 = n3
if(f1>f2):
    print(str(f1) + " is the greatest")
else:
    print(str(f2) + " is the greatest")
    