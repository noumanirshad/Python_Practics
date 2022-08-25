import random
def gamewin(com, you):
    if com == you:
        return None
    elif com == 's':
        if you == 'g':
            return True
        elif you == 'w':
            return False
    elif com == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
    elif com == 'g':
        if you == 'w':
            return True
        elif you == 's':
            return False

randNo = random.randint(1,3)

print("Select in one option: \nSnake(s) Water(w) Gun(g)")
if randNo == 1:
    com = 's'
elif randNo == 2:
    com = 'w'
elif randNo == 3:
    com = 'g'
you = input("Enter the one option: 's' , 'w' , 'g' ")
print(f"Computer selected a {com}")
print(f"You select a {you}")
 

f = gamewin(com , you)
if f == None:
    print("This match is tie: plz next try")
elif f:
    print("you win")
else:
    print("you lose")
