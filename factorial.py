def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        f = num * (factorial(num -1))
        return f

number = int(input("Enter the number: "))
fac = factorial(number)
print(f"Fact of {number} is [{fac}]")

