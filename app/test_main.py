from app.main import get_coin_combination


import pytest
from app.main import get_coin_combination

def test_one_penny():
    assert get_coin_combination(1) == [1, 0, 0, 0]

def test_one_nickel():
    assert get_coin_combination(5) == [0, 1, 0, 0]

def test_mixed_coins():
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(6) == [1, 1, 0, 0]

def test_exact_quarters():
    assert get_coin_combination(50) == [0, 0, 0, 2]

def test_no_coins():
    assert get_coin_combination(0) == [0, 0, 0, 0]

def test_large_amount():
    assert get_coin_combination(99) == [4, 0, 2, 3]

def test_invalid_negative_input():
    with pytest.raises(ValueError):
        get_coin_combination(-5)

