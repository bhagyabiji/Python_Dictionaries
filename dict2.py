
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964,
    "colors" : ["red","blue","black"]
}
print(thisdict)

print("\n-------------------")

#for in loop
for x in thisdict:
    print(x)

print("\n-------------------")

#Print all values in the dictionary, one by one
for x in thisdict:
    print(thisdict[x])

print("\n-------------------")

#can also use values()
for x in thisdict.values():
    print(x)

print("\n-------------------")

#keys()
for x in thisdict.keys():
    print(x)

print("\n-------------------")

#items()-returns both keys and values
for x,y in thisdict.items():
    print(x,y)

print("\n-------------------")
