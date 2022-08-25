# f = open("twinkly.txt", "r")
# d = f.read()
# if "star" in d:
#     print("this is present")
# else:
#     print("this is not present")
# f.close()



f = open("twinkly.txt", "r")
d = f.read()
if "twSS" in d:
    with open("twinkly.txt", "a") as e:
        e.write("\nNouman Programmer")
else:
    with open("twinkly.txt", "a") as e:
        e.write("\nNUMI Programmer")
f.close()

