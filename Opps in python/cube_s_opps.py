class Calculator:
    num_square = int(input("Enter the number of square: "))
    num_cube = int(input("Enter the number of cube: "))
    num_s_root = int(input("Enter the number of squareroot: "))

        
    def square(self, s):
        print(f"\nSquare of {s} is: {s**2}") 
    def cube(self, c):
        print(f"Cube of {c} is: {c**3}") 
    def s_root(self, b):
        print(f"SquareRoot of {b} is: {b**0.5}") 

num =   Calculator()
num.square(num.num_square)
num.cube(num.num_cube)
num.s_root(num.num_s_root)