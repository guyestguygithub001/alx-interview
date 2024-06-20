#!/usr/bin/python3

"""This script defines a function `makeChange` that calculates the minimum number of coins needed to make a specific amount.

The function takes two arguments:
  - `coins`: A list of integers representing the denominations of the available coins.
  - `total`: An integer representing the target amount to be made.

The function returns:
  - An integer representing the minimum number of coins needed to make the target amount, or
  - -1 if it's impossible to make the target amount with the given coins.
"""


def makeChange(coins, total):
    """Calculates the minimum number of coins needed to make a specific amount.

    Args:
      coins: A list of integers representing the denominations of the available coins.
      total: An integer representing the target amount to be made.

    Returns:
      An integer representing the minimum number of coins needed to make the target amount, or
      -1 if it's impossible to make the target amount with the given coins.
    """

    if total <= 0:
        return 0

    rem = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)

    while rem > 0:
        if coin_idx >= n:
            return -1
        if rem - sorted_coins[coin_idx] >= 0:
            rem -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1

    return coins_count

