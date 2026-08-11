def Yash():
    s = input("camelCase: ")
    t = ""
    for c in s:
        if c.isupper():
            t += "_" + c.lower()
        else:
            t += c
    print("Snake_case: ", t)

Yash()