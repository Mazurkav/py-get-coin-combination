# app/main.py

def get_coin_combination(cents: int) -> list:
    """
    Calculate the smallest combination of coins for a given amount in cents.

    The function returns a list where:
    - coins[0] = number of pennies (1 penny = 1 cent)
    - coins[1] = number of nickels (1 nickel = 5 cents)
    - coins[2] = number of dimes (1 dime = 10 cents)
    - coins[3] = number of quarters (1 quarter = 25 cents)

    Args:
        cents (int): The total amount in cents to convert into coins.

    Returns:
        list: A list representing the smallest combination.
            The list contains [pennies, nickels, dimes, quarters].
    """
    values = [1, 5, 10, 25]
    coins = [0, 0, 0, 0]

    for i in range(3, -1, -1):
        coins[i] = cents // values[i]
        cents -= coins[i] * values[i]

    return coins
