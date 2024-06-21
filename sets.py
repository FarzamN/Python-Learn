'''
 Set will not let you store duplicate values
 Sets are unIndexed
 Can not remove item from sets
 Sets are mutable
 Sets are unordered
'''
s = {1,"213", "Hello","Hello"}
sNew = {12,"321", "Hello","world","new"}
emp = set() # this is the empity set
print(emp)

s.remove("213") # will remove perticular item from set
# print(s.union(sNew)) # will print combine value from s and sNew
# print(s.intersection(sNew)) # will print common items from both sets
print(s.isdisjoint(sNew)) # will check if any common items are present in both sets