user = None
while(user != 2):
    fahrenheit = int(input("Enter temperature in fahrenheit: "))
    cel = 6*(fahrenheit - 32)/9
    print(f"Temperature in celculies: {cel}")
    print("\n\t1: For continue *******\n\t2: For exit ******* ")
    user = int(input("Enter the number: "))
    if(user ==2):
        print("\n\tThank you for using this program ******\n")