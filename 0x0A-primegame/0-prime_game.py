#!/usr/bin/python3
"""Module for determining the winner of the Prime Game."""

def isWinner(x, nums):
    """
    Determines the winner of a Prime Game session with 'x' rounds.
    
    Args:
    x (int): Number of rounds in the game.
    nums (list): List of upper bounds for each round.
    
    Returns:
    str or None: 'Maria', 'Ben', or None in case of a tie or invalid input.
    """
    if x < 1 or not nums:
        return None
    
    marias_wins, bens_wins = 0, 0
    
    # Generate a list of primes up to the maximum number in nums
    n = max(nums)
    primes = [True] * n
    primes[0] = False
    
    # Sieve of Eratosthenes to mark non-prime numbers
    for i in range(2, int(n**0.5) + 1):
        if primes[i - 1]:
            for j in range(i*i, n + 1, i):
                primes[j - 1] = False
    
    # Count primes for each round and determine the winner
    for round_num in nums[:x]:
        prime_count = sum(primes[:round_num])
        if prime_count % 2 == 0:
            bens_wins += 1
        else:
            marias_wins += 1
    
    # Determine the overall winner
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
