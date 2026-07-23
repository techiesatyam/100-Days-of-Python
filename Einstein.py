#Using a function to Calculate the energy using Einstein equation.
def Phy(M =  float(input("Enter the mass in (Kg): "))):
    C = 3*10**8
    return(M*C**2)
  

Energy = Phy()
print(Energy)