name = input("What's your name? ")

file = open("name.txt", "a")
file.write(f"{name}\n")
file.close()

names = []
with open("name.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}!") 