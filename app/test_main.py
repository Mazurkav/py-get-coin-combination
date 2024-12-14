# test_main.py
from main import get_coin_combination

def test_get_coin_combination() -> None:
    # Test case 1: 1 penny
    assert get_coin_combination(1) == [1, 0, 0, 0]

    # Test case 2: 6 cents (1 penny + 1 nickel)
    assert get_coin_combination(6) == [1, 1, 0, 0]

    # Test case 3: 17 cents (2 pennies + 1 nickel + 1 dime)
    assert get_coin_combination(17) == [2, 1, 1, 0]

    # Test case 4: 50 cents (2 quarters)
    assert get_coin_combination(50) == [0, 0, 0, 2]

    # Test case 5: 99 cents (4 quarters + 2 dimes + 0 nickels + 4 pennies)
    assert get_coin_combination(99) == [4, 0, 2, 3]

    # Test case 6: 100 cents (4 quarters)
    assert get_coin_combination(100) == [0, 0, 0, 4]

    # Test case 7: 1 cent (just a penny)
    assert get_coin_combination(1) == [1, 0, 0, 0]

    # Test case 8: 4 cents (4 pennies)
    assert get_coin_combination(4) == [4, 0, 0, 0]

    # Test case 9: 25 cents (1 quarter)
    assert get_coin_combination(25) == [0, 0, 0, 1]

    # Test case 10: 30 cents (1 quarter + 1 nickel)
    assert get_coin_combination(30) == [0, 1, 0, 1]
