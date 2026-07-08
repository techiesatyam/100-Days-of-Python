# This program asks user for name and greets them.

name = input("What's your name? ")

# Remove white space from the str.
name = name.strip().title()

# Split the name into first and last name
first, last = name.split(" ")

print(f"Hello, {first}")

# Using escape characters to include quotes in the output

print("Hello, \"friend\"")