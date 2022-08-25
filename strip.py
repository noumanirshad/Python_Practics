# def strip(name):
#     return(name.strip())

# x = "   This is numi programer:     "
# print(strip(x))

def strip(string, rep):
    f = x.replace(rep, "")
    return(f.strip())

x = "   This is numi programer:     "
this = strip(x, "This")
print(this)