def Avishi():
    answer = input("What is the answer to Great question of life, the Universe, and Everything? ")
    if answer == "42" or answer == "forty-two" or answer == "forty two":
        return("Yes")
    else:
        return ("No")

print(Avishi())