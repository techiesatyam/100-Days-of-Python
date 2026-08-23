def ine():
    x = get_int("Enter a number: ")
    print(f"The result of division is: {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
        
ine()   