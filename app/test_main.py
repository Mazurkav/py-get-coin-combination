# tests/test_main.py

import pytest
from app.main import get_coin_combination


def test_one_penny() -> None:
    """Test case for 1 penny"""
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_one_nickel() -> None:
    """Test case for 1 nickel"""
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_one_dime() -> None:
    """Test case for 1 dime"""
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_one_quarter() -> None:
    """Test case for 1 quarter"""
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_mixed_coins() -> None:
    """Test case for mixed coins"""
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_exact_quarters() -> None:
    """Test case for exactly 2 quarters"""
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_no_coins() -> None:
    """Test case for no coins"""
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_large_amount() -> None:
    """Test case for a large amount"""
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_high_value() -> None:
    """Test case for a higher value"""
    assert get_coin_combination(123) == [3, 0, 2, 4]


def test_invalid_input() -> None:
    """Test case for invalid negative input"""
    with pytest.raises(ValueError):
        get_coin_combination(-5)
