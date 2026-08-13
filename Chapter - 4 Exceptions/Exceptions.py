def ine():
    x = get_int()
    print(f"The result of division is: {x}")

def get_int():
    while True:
        try:
            x = int(input("Enter a number: "))
        except ValueError:
            print("Invalid input!\nPlease enter valid integers.")
        else:
            return x
        
ine()   