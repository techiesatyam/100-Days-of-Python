from twttr2 import shorten

def test_one():
    assert shorten("Hello, World!") == "Hll, Wrld!"

def test_two():
    assert shorten("Day 2") == "Dy 2"