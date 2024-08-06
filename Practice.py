import numbers
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

# 2) Write a program to input eight numbers from user and display the all unique numbers 

sets = set()
for i in range(3):
    n = input(f"Enter 0{i+1} number: ")
    sets.add(n)
print(f"Here is the final value {sets}")

# 3) Can we have a set with 18(int) and "18"(str) as a value in it?
 
sets = {18, "18"}
print(sets) # it will print both values as it is set

# 4) What will be the length of the following set Sets

Sets = {18, "18",18.00}
print(len(Sets)) # flooting number will be = 18

# 5) create an empty dictionary. Allow 4 friends to enter their favourite language and include the names of your friends in the dictionary. Print the dictionary

favLang = {}

for i in range(2):
    name = input(f"Enter your Name {i+1}: ")
    lang = input(f"Enter your Favourite Language {i+1}: ")
    # favLang[name] = lang
    favLang.update({name:lang})

    print(favLang)

# 6) Change value of array

s = {1,2,3,4,"Farzam", [1,2]}
print(type(s))

# for and while loop Practice
# 1) Write a program to print multiplication table of a given no. using for loop

num = int(input("Enter a number: "))

for i in range (1,11):
    print(f"{num} x {i} = {num * i}")

# 2) White a program to greet all the person names stored in a list and which starts with S
listing = ["Harry", "Soham","Sachin","Rahul"]

for i in listing:
    if (i.startswith("S")):
       print(f"Hello {i}")

# 3) Write a program to print multiplication table of a given no. using while loop

num = int(input("Enter a number: "))
table = 1
while (table <= 10):
    print(f"{num} x {table} = {num * table}")
    table += 1

# 4) Write a program to find wheather a given number is prime or not

num = int(input("Enter a number: "))

for i in range(2, num):
    if (num%i) == 0:
        print("prime number")
        break
    else: 
        print("false")
        break

# 5) write a program to find the sum of first natural number
num = int(input("Enter a number: "))
i = 1
sum = 0
while (i<= num):
    sum += i
    i+=1

print(sum)

# Function and Recuration loop Practice

# 1) write a program using function to find greatest of three numbers.

def greatNum(a,b,c):
    if(a > b and a>c):
       return a
    elif(b>c and b>a):
        return b
    elif(a>b and b> a):
        return c
    
a = 1
b = 23
c =3    

print(greatNum(50,100,c))

# 2) write a python program using function to convert Celsius to Fahrenheit.

def toFahrenheit(cel):
    f = cel * (9/5) + 32
    return f

Celsius = 50
print(toFahrenheit(Celsius))

# 3) How do you prevent a python print() function to print a new line at the end.

print("a")
print("b")
print("c", end="")
print("d", end="")

# 4) Write a recursive function to calculate the sum of first n natural numbers.

def rec(n):
    if( n ==1) :
        return 1
    return rec(n-1) + n


print(rec(0))
# 5) Write a python function to print first n lines of the following pattern:
# ***
# **
# *            -for n=3

def printStar(n):
    if(n ==0):
        return 
    print("*" * n)
    printStar(n-1)

printStar(3)

"""
# 6) Write a python function to remove a given word from a list ad strip it at the same time
