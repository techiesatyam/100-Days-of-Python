from Hello import hello;

def test_one():
    assert hello("Satyam") == "Hello, Satyam!"

def test_two():
    for name in ["Alice", "Bob", "Charlie"]:
        assert hello(name) == f"Hello, {name}!"