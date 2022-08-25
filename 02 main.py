num = int(input("Enter the number: "))
prime = False
for i in range(2, num):
    if num%i == 0:
        prime = True
        break
if prime:
    print('This number is not prime')
else:
    print("This number is prime")