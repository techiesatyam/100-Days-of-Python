def grocery():
    list = {}

    try:
        
        while True:
            item = input().strip().upper()
            if item in list:
                list[item] += 1
            else:
                list[item] = 1

    except(EOFError):
        print("")

    for item in sorted(list):
        print(f"{list[item]}, {item}")
        
grocery()