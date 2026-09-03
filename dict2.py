
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

#copy() method
mydict = thisdict.copy()
print(mydict)

print("\n-------------------")

#dict() - to copy a dict
mydict = dict(thisdict)
print(mydict)

print("\n-------------------")

#nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

print("\n-------------------")

#Access Items in Nested Dictionaries
print(myfamily["child2"]["year"])

print("\n-------------------")

#Loop Through Nested Dictionaries
for x,obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ":" , obj[y])

#Create a dictionary with 3 keys, all with the value 0
x = ('key1','key2','key3')
y = 0
thisdict = dict.fromkeys(x,y)
print(thisdict)