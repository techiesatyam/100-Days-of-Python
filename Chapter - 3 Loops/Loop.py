#Defining a function for while loop
def Call(): 
    O = 0
    while O < 3:
        print("Bye")
        O = O + 1
Call()

# Using for loop
for i in [0, 1, 2]:
    print(i)

#Using while and for loop together
def UIX():
    while True:
        y = int(input("What's y? "))
        if y < 0:
            continue
        else:
            break

    for _ in range(y):
        print(f"Goodbye! {y}")

UIX()

# Using length function 
planets = ["Saturn", "Jupiter", "Mars", "Earth"]

for i in range(len(planets)):
    print(i + 1, planets[i])

# Dictionary loop
fruits = {
    "Apple": "Kashmiri",
    "Mango": "Alphonso, Kesar",
    "Guava": "Sardar",
    "Lichi": "Chinese"
}
for f in fruits:
    print(f, fruits[f], sep=": ")

# Using for loop for multiple dictionaries.
vegetables = [
    {"name": "Potato", "type": "Root"},
    {"name": "Spinach", "type": "Leafy"},
    {"name": "Carrot", "type": "Root"}
]
for v in vegetables:
    print(v["name"], v["type"], sep=": ", end="\n")

# Mario game using "for" loop
def Mario():
    print_column(3)
    print_row(4)

def print_column(height):
    for _ in range(height):
        print("#", end="")

def print_row(width):
        print("?" * width, end="\n")
Mario()