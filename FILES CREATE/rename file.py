import os
f1 = "simple2.txt"
f2 = "new name.txt"
with open(f1) as f:
    contant = f.read()

with open(f2, "w") as f:
    f.write(contant)
os.remove(f1)
