for i in range(4):
    try:
        x = int(input("Enter a number: "))
        y = int(input("Enter another number: "))
        result = x / y
        print("The result of division is:", result)
        break

    except ValueError:
        print("Invalid input! Please enter valid integers.")
        continue