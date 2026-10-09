from calculator import cube

def test_cube():
    if cube(2) != 8:
          print("Error!\n2 cubed is not 8.")
  
    if cube(45) != 91125:
          print("Error!\n45 cubed is not 91125.")
  
    else:
          print("All tests passed!")

test_cube()