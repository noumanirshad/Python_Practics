mydict = {
    "books" : "English, Maths , Programing, Calculas, Computing",
    "books" : "physics",
    "friends": "maviya , Marig, Muneeb, Hammad",
    1: 343
}
f = mydict[1]
mydict["friends"]= {"saqib , farhan , raheel"}
print(mydict["books"])
# print(mydict.keys())
# print(mydict.values())
# print(mydict.items())
udat  = {
    "name" : "nouman",
    "list" : [3,4,5]
}
mydict.update(udat)
print(mydict)