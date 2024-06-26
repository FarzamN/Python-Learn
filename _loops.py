'''
for i in range(1, 11):
    print(f"for ka data {i}")

i = 1
while i >= 10:
    print(f"while ka data {i}")
    i += 1

listItem = ["Farzam", "Nawal", "Faaz", "Nuflah", "Nasheeta", "Nareeman"]
listItem = [1,34]
listIndex= 0
while listIndex < len(listItem):
    print(f"while ka data {listItem[listIndex]}")
    listIndex += 1

for i in range (len(listItem)):
    print(f"for ka data {listItem[i]}")
for i in (listItem):
    print(f"for ka data {i}")

for item in "hello":
    print(item)
else :
    print("Done")

for i in range(11):
    if i == 5:
       continue
    print(f"for ka data {i}")
'''

for i in range(11):
    if i == 5:
       break
    print(f"for ka data {i}")