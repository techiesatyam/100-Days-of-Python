from calculator import cube

def test_cube():
    assert cube(2) == 8
    assert cube(3) == 27
    assert cube(4) == 64

test_cube()