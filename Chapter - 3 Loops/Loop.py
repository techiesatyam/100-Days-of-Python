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