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

x = float(input("Value of x: "))
y = float(input("Value of y: "))

if x > y or x < y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# Making the code more simpler
if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")

# Defining a function to assign students grade on the basis of their score
def Grade (score):
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
    elif score > 100 and score < 5:
        print("Invalid Grade")
    else:
        print("Grade: F-")
Grade(int(input("Score: ")))

# Using Boolean Conditionals to check if a number is even or odd
def main(e):
    if even(e):
        print("Even no.")
    else:
        print("Odd no.")

def even(e):
    if e % 2 == 0:
        return True
    else:
        return False
    
main(int(input(" What's e? ")))