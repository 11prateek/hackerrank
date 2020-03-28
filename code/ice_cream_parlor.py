"""
https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem
"""

import math
import os
import random
import re
import sys


# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    hash = dict()

    for i in range(len(cost)):
        hash.update(
                    {cost[i]:i+1}
        )

    for i in range(len(cost)):
        first_flavour = i + 1
        second_flavour = hash.get(money - cost[i], None)

        if first_flavour == second_flavour:
            continue

        if second_flavour is not None:
            print(first_flavour, second_flavour)
            break


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
