# Using if, elif, and else statements to compare two numbers

x = int(input("What's x: "))
y = int(input("What's y: "))

if x > y:
    print("x is greater than y")

elif x < y:
    print("x is less than y")

else:
    print("x is equal to y")

# Using or conditionals

x = float(input(" Value of x: "))
y = float(input(" Value of y: "))

if x > y or x < y:
    print("x is not equal to y")
else:
    print("x is equal to y")