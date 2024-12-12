def get_coin_combination(cents: int) -> list:
    """
    Calculate the smallest combination of coins for a given amount in cents.
    Returns a list: [pennies, nickels, dimes, quarters].
    """
    values = [1, 5, 10, 25]
    coins = [0, 0, 0, 0]

    for i in range(3, -1, -1):
        coins[i] = cents // values[i]
        cents -= coins[i] * values[i]

    return coins
