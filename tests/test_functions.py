import pytest

# Import learner's functions from exercises.py
from exercises import greet, add_numbers, calculate_area


def test_greet_basic():
    """Check that greet returns correct string"""
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"


def test_add_numbers_basic():
    """Check addition of two positive integers"""
    assert add_numbers(2, 3) == 5
    assert add_numbers(10, 0) == 10


def test_add_numbers_edge_cases():
    """Check addition with negatives and large numbers"""
    assert add_numbers(-1, 5) == 4
    assert add_numbers(1_000_000, 1) == 1_000_001


def test_calculate_area_square():
    """Check area of a square"""
    assert calculate_area(5, 5) == 25


def test_calculate_area_rectangle():
    """Check area of a rectangle"""
    assert calculate_area(2, 10) == 20


def test_calculate_area_edge_cases():
    """Check area with zero and negative values"""
    assert calculate_area(0, 10) == 0
    assert calculate_area(3, -4) == -12  

