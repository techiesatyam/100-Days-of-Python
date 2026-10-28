from modulefinder import test

from calculator import cube

def test_positive():
    assert cube(2) == 8
    assert cube(3) == 27
    assert cube(4) == 64

def test_negative():
    assert cube(-2) == -8
    assert cube(-3) == -27
    assert cube(-4) == -64