# Defining a function for greeting .
def Main(Formal):
     
    match Formal:
        case "Hello" | "Hello, Newman":
            return("$0")
        case "Hey" | "How are you doing?" | "How's it going?":
            return("$20")
        case "What's happening?" | "What's up?":
            return("$100")
        case _:
            return("Sorry! we didn't get you")        
       
print(Main(input("Greeting: ")))