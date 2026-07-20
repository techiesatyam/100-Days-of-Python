# Trying to understand the return here.
def main():
    Bill_total = int(input("Bill total: $ "))
    print("Bill cost is $", Bill_total)
    return Bill_total # What work this return is doing here?
main()

# Creating a function to calculate bill of the customer's meal.
def calculus():

    Bill_amount = float(input("Bill amount: $ "))
    GST_percentage = float(input("GST %: "))
    GST = (GST_percentage / 100) * Bill_amount
    Total = round(Bill_amount + GST, 2)
    GST_amount = round(Total - Bill_amount, 2)
    print(f"Total bill for meal is: ${Total}")
    print(f"GST amounrt added is: ${GST_amount}")

calculus() 