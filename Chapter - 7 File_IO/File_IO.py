def read_names():
    names = []
    with open("name.csv", "r") as file:
        for line in file:
            row = line.rstrip().split(",")

        print("Reading:", row)
        print("Length:", len(row))

        if len(row) == 2:
            names.append(f"{row[0]} is in {row[1]}")

    print("Final list:", names)

    return names