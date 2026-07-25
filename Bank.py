# Defining a function for greeting .
def Main():
    Formal = input("Greeting: ")
    if Formal == "Hello" or Formal == "Hello, Newman":
        return("$0")
    elif Formal == "Hey" or Formal == "How you doing?" or Formal == "How's it going?":
        return("$20")
    elif Formal == "What's happening?" or Formal == "What's up?":
        return("$100")
    else:
        return("Sorry!!, Invalid greeting")
               
print(Main())