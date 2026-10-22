from plates_2 import print_valid

def test_dl():
    assert print_valid("C4") == False
    assert print_valid("4C") == False

def test_ban():
    assert print_valid("50") == False
    assert print_valid("CS/&") == False

def test_neural():
    assert print_valid("CS50") == True
    assert print_valid("CS50P") == True

def test_ml():
    assert print_valid("CS50P1") == True
    assert print_valid("CS50P2") == True