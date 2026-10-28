def main():
    convert()
    gauge()

def convert(numerator, denominator):
    return numerator / denominator

def gauge(numerator, denominator):
    while True:
        try:
            if numerator > denominator:
                continue
            percentage = round(numerator / denominator * 100)
            break

        except (ValueError, ZeroDivisionError):
            continue

    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"Fuel: {percentage}%")

if __name__ == "__main__":
    main()