# main.py
from typing import List


def get_coin_combination(cents: int) -> List[int]:
    coins = [0, 0, 0, 0]  # [pennies, nickels, dimes, quarters]

    coins[3] = cents // 25  # Quarters
    cents %= 25

    coins[2] = cents // 10  # Dimes
    cents %= 10

    coins[1] = cents // 5  # Nickels
    cents %= 5

    coins[0] = cents  # Pennies

    return coins
