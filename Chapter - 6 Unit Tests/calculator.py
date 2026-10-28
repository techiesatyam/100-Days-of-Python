def main():
    x = int(input("What is the value of x? "))
    print ("X cubed is ", cube(x))

def cube(n):
    return n ** 3

if __name__ == "__main__":
    main()