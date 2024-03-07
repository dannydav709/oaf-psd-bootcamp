# import pytest
from .script import is_prime


def test_prime_numbers():
    assert is_prime(4) == False
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(17) == True
    assert is_prime(19) == True
    
    assert is_prime(23) == True
    assert is_prime(29) == True

    


def test_non_prime_numbers():
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(9) == False
    assert is_prime(16) == False
