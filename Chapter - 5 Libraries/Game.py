import random

def game():

    while True:
        try: 
            n = int(input("Level: "))
            if n > 0:
                break
        except ValueError:
            pass
    number = random.randint(1, n)
    while True:
        guess = input("Guess: ")
        try:
            guess = int(guess)
            if guess < number:
                print("Too small!")
                break
            elif guess > number:
                print("Too large!")
                break
            else:
                print("Just right!")
                break
        except ValueError:
            pass

game()