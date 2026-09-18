import inflect

def hollow():
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)

            if len(names) == 1:
                print(f"Adieu, adieu, to {names[0]}")
                break
            elif len(names) == 2:
                print(f"Adieu, adieu, to {names[0]} and {names[1]}")
                break
            else:
                print(f"Adieu, adieu, to {', '.join(names[:-1])}, and {names[-1]}")
                break
        except EOFError:
            print()
            break
hollow()