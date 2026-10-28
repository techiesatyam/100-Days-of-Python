from fuel_2 import convert, gauge 

def test_my_fuel_1():
    assert convert(1, 2) == 0.5

def test_my_fuel_2():
    assert gauge(1, 2) ==  None