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

# Making the code more simpler
if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")

# Using and condition to assign students grade 
score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("Grade: A1")
elif score >= 80 and score < 90:
    print("Grade: A2")
elif score >= 70 and score < 80:
    print("Grade: B2")
elif score >= 60 and score < 70:
    print("Grade: C1")
elif score >= 50 and score < 60:
    print("Grade: C2")
elif score >= 40 and score < 50:
    print("Grade: D")
else:
    print("Grade: F-")