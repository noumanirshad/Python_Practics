with open("name.txt") as f:
    g = f.read()
    with open("name2.txt", "w") as f:
        f.write(g)