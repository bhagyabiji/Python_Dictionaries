
#creating a dictionary
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964,
    "colors" : ["red","blue","black"]
}
print(thisdict)

#Print the "brand" value of the dictionary
print(thisdict["brand"])

#using len() method
print(len(thisdict))

#type() method
print(type(thisdict))

#to make a dict using dict() constructor
thisdicty = dict(name = "john", age = 22, country = "India")
print(thisdicty)

#Get the value of the "model" key
print(thisdict["model"])

#can also use get()
x = thisdict.get("year")
print(x)

#to get all the keys in the dict
m = thisdict.keys()
print(m)

print("\n--------------")

#Add a new item to the original dictionary, and see that the keys list gets updated
print(thisdict.keys())
thisdict["automatic"] = "YES"
print(thisdict)

print("\n--------------")

a = thisdict.values()
print(a)

#Make a change in the original dictionary, and see that the values list gets updated 
thisdict["year"] = 2020
print(a)

print("\n--------------------")

#Get a list of the key:value pairs
b = thisdict.items()
print(b)

print("\n--------------------")
#check if key exist
if "model" in thisdict:
    print("yes. I am here")

print("\n--------------------")
thisdict["year"] = 2018
print(thisdict)

print("\n--------------------")
#Update the "year" of the car by using the update() method
thisdict.update({"year" : 2019})
print(thisdict)


print("\n--------------------")

#using pop()
thisdict.pop("automatic")
print(thisdict)

#popitem() -removes the last inserted item
thisdict.popitem()
print(thisdict)

print("\n--------------------")

#del keyword removes the item with the specified key name
del thisdict["year"]
print(thisdict)

print("\n--------------------")

#clear() - will empty the dict 
thisdict.clear()
print(thisdict)

print("\n--------------------")

# del - if not specify the key then the dict will be deleted
del thisdict
print(thisdict)
