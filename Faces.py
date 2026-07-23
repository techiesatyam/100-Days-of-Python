#Creating a function which convert emoticons to emoji
def convert(Code):

    Code = Code.replace(":)", "🙂").title()
    Code = Code.replace(":(", "🙁").title()
    print(Code)

convert(input("Enter the text: "))