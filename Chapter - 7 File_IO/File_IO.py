name = input("What's your name? ")

file = open("name.txt", "a")
file.write(f"{name}\n")
file.close()
