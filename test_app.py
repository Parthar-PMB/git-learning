from app import greet

def test_greet():
    assert greet("Partha") == "Hello, Partha!"

def test_greet_returns_string():
    assert isinstance(greet("anyone"), str)