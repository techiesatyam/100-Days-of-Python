def vishnu():
    t = input("Input: ")

    for q in t:
        if q not in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]:
            print(q, end="")

vishnu()