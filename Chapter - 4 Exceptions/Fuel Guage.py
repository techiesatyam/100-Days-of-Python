def jin():
    while True:

        try:
            n = input("Fraction: ")
            x, y = n.split("/")

            x = float(x)
            y = float(y)

            if x > y:
                continue
            percentage = round(x / y *100)
            break

        except (ValueError, ZeroDivisionError):
            continue

    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"Fuel: {percentage}%")

jin()