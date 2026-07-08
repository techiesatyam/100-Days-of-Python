# This program asks user for name and greets them.

name = input("What's your name? ")

# Remove white space from the str.
name = name.strip()

#Capitalize the first letter of the name.
name = name.capitalize()

print(f"Hello, {name}!")

# Using escape characters to include quotes in the output

print("Hello, \"friend\"")