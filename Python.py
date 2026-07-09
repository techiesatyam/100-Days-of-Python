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

print(round(x + y))

# Subtraction Operator
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

print(x - y)

