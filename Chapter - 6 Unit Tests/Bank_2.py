def main():
    value()

def value(greeting):
     
    match greeting:
        case "Hello" | "Hello, Newman":
            return("$0")
        case "Hey" | "How are you doing?" | "How's it going?":
            return("$20")
        case "What's happening?" | "What's up?":
            return("$100")
        case _:
            return("Sorry! we didn't get you")        


if __name__ == "__main__":
    main()  