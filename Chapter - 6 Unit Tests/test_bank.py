from Bank_2 import value

def testing_one():
    assert value("Hello") == "$0"
    assert value("Hello, Newman") == "$0"
def test_two():
    assert value("Hey") == "$20"
    assert value("How are you doing?") == "$20"
def test_third():
    assert value("How's it going?") == "$20"
    assert value("Good morning") == "Sorry! we didn't get you"