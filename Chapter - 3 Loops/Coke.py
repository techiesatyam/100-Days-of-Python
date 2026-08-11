def nick():
    Amount = 50

    while Amount > 0:
        print(f"Amount Due: {Amount}")
        coin = int(input("Insert Coin: "))

        if coin in [5, 10, 15, 20, 25]:
           Amount = Amount - coin
        else:
            print("Invalid Coin")

    print("Change owed: ", -Amount)

nick()  