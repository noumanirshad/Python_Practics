x = (input('Enter the number: '))
try:
  print(x*2)
except:
  print("Something went wrong.")
finally:
  print("The 'try except' is finished")