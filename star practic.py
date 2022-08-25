a = 3
for i in range(a):
    # print(' '*    )
    print("*"*a)
print(f"* {''*a-1} *")
print("*"*a)

 
a = int(input("Enter the number: "))
def star(n):
    for i in range(n):
        print((n-i) * "*")
f = star(a)
print(f)