x = int(input("Enter the first number: "))
evl = input("Enter the operator: ")
y = int(input("Enter the second number: "))

def add(x,y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def devide(x, y):
    if y == 0:
        return "can not devide by 0"
    return x / y

def calculator(x, evl, y):
    if evl == "+":
        return add(x, y)
    elif evl == "-":
        return subtract(x, y)
    elif evl == "*":
        return multiply(x, y)
    elif evl == "/":
        return devide(x, y)
    else:
        return "Invalid operator"
    
print(calculator(x, evl, y))
