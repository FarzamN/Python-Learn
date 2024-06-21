# dictionary is like json for example
students = {
    "Farzam": 100,
    "Faaz": 10,
    "Fahad": 500,
}

# now to print
# print(students["Farzam"])

# Properties

"""
 • It is unordered (order doesnot metter)
 • It is mutable (you can add edit perticular item)
 • It is indexed (will not check every item)
 • Can't contain same key
"""

# print("Keys",students.keys())
# print("values",students.values())
# print("items",students.items())

# students["Fahad"] = 600 # to update perticular key
# students.update({"Faaz": 600,"Rohan": 10}) # to update perticular key


# print(students.get("Not Found")) # if not found then this will return none

students.popitem() # will remove the last item from dictionary
students.pop("Fazz") # will remove the past item from dictionary

print(students)
