#!/usr/bin/python3
'''Given a pile of coins of different values,
    determine the fewest number of coins needed to meet
    a given amount total.
'''

def makeChange(coins, total):
    '''
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    '''
    memo = {}
    
    def helper(total):
        if total <= 0:
            return 0
        if total in memo:
            return memo[total]
        min_coins = float('inf')
        for coin in coins:
            if coin <= total:
                subres = helper(total - coin)
                if subres != -1 and subres + 1 < min_coins:
                    min_coins = subres + 1
        memo[total] = -1 if min_coins == float('inf') else min_coins
        return memo[total]
    
    return helper(total)