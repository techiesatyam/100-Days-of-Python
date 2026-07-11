# This program asks user for name and greets them.

name = input("What's your name? ")

# Remove white space from the str.
name = name.strip().title()

print(f"Hello, {name}")

# Using escape characters to include quotes in the output
print("Hello, \"friend\"")

#Arithmatic operations

#Addition Operator using int operator
x = int(input("Enter the number: "))
y = int(input("Enter the number: "))

print(x + y)

# Addition Operator using float and round off operator
x = float(input("Enter number: "))
y = float(input("Enter number: "))

print(round(x + y, 2))

# Subtraction Operator
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

print(x - y)

# Multiplication Operator
x = float(input("Enter a number: "))
y = float(input("Enter a number: "))

print(round(x * y, 2))

# Creating our own function to perform division operation
def divide(x,y):
    return x / y

x = float(input("Enter a number: "))
y = float(input("Enter a number: "))

print(round(divide(x, y), 2))