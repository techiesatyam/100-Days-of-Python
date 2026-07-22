# Asking user for their name by creating a function.
def cal(YOB, Year):
    print(f"This is coming from below cal {YOB}")
    name = input("What's your good name? ")
    name = name.strip().title()
    print(f"Hello , {name}. How are you doing?")

# Calculating user age in year they want.
    Age = Year - YOB

    print(f"Your age in {Year} year will be {Age} years old.")

cal(Year = int(input("What's the year you want to know your age? ")), YOB = int(input("What's your birth year? ")))