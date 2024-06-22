"""
# 1) Write a program to store seven fruits in a list entered by user.

fruits = []
# a = input("enter Fruits Name: ")
# fruits.append(a)
# b = input("enter Fruits Name: ")
# fruits.append(b)
# print(fruits)

# Chat GPT answer in Short ==========================
for i in range(2):
    fruit = input(f"Enter the name of fruit {i+1}: ")
    fruits.append(fruit)

print(f"The list of fruits you entered is: {fruits}," )

# 2) Write a program to accept mark of 6 students and display them in a sorted manner.

marks = []

for i in range(2):
    Number = float(input(f"Enter the Make of Student {i+1}: "))
    marks.append(Number)

# print(f"The list of Numbers you entered is: {marks.sort()}," )

# 3) Check that tuple type cannot be change in python

tup = (1,23,"sdfs")

tup[1] = 100

print(tup)
# 4) Write a program to sum a list with 4 numbers.

sumList = [1,2,3,4,1]
print(sum(sumList))
# 4) Write a program to count number of zer in following tuple
# a = (7,0,8,0,0,9)
countTup = (7,0,8,0,0,9)
counted= countTup.count(0)
print(counted)

"""

# Dictionary and Sets Practice
# 1) Write a program to create a dictionary of Hindi words with values as their English translation. Provide the user an option to look up the meaning of a word.

words = {
    "cat": "Billi",
    "dog": "kutta",
    "snake": "Sanp",
    "Butcher": "Kasai"
}

word = input("Enter a word: ")
print(words.get(word, "Word not found in Words"))