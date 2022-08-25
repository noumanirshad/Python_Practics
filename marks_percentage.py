num1 = int(input("Enter the number of marks 1 "))
num2 = int(input("Enter the number of marks 2 "))
num3 = int(input("Enter the number of marks 3 "))
num4 = int(input("Enter the number of marks 4 "))

total = (num1+num2+num3+num4)/4
if(total >= 90):
    print("Ex")
elif(total >= 80):
    print("A")
elif(total >= 70):
    print("B")
elif(total >= 60):
    print("C")
elif(total >= 50):
    print("D")
elif(total <= 50):
    print("F")
if (num1<50 or num2<50 or num3<50 or num4<50):
    print("your are fail because your 1 subject marks less than 50")
elif(total<50):
    print("your are fail because your total percentage less than 50")
else:
    print("Congratulations: Your are pass.")
    