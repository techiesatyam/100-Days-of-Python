import random

def get_level():
    while True: 
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3, 4]:
                return n
        except (ValueError):
            pass

def generate_integer(level):
    if level not in [1, 2, 3, 4]:
        raise ValueError

    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        return random.randint(1000, 9999)

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        for _ in range(3):
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == answer:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(f"{x} + {y} = {answer}")
    print(f"Score: {score}")

if __name__ == "__main__": 
    main()