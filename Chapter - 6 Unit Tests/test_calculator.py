from calculator import cube

def test_cube():
    try:
        assert cube(2) == 8
        print("Test passed!")
    except AssertionError:
        print("Sorry!\nTest Failed!")

    try:
        assert cube(3) == 27
        print("Test passed!")
    except AssertionError:
        print("Sorry!\nTest Failed!")

test_cube()