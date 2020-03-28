'''
https://www.hackerrank.com/challenges/new-year-chaos/problem
'''

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
    """
    Takes a list and prints the solution as
    described by the ``New Year Chaos`` problem.

    Parameters:
    ----------
        q: list
    """
    # Keep track of bribes for each individual
    n_bribes = [0] * len(q)

    while True:
        bribe_occured = False

        # For each round:
        # 1. Check if each element is larger than the element after it
        # 2. If each element can still bribe
        for i in range(len(q) - 1):
            if q[i] > q[i+1] and n_bribes[q[i] - 1] < 2:
                # Keep track of number of bribes paid
                n_bribes[q[i] - 1] = n_bribes[q[i] - 1] + 1

                # Swap elements
                q[i], q[i+1] = q[i+1], q[i]

                # Keep track if bribe occured this round
                bribe_occured = True

        # If no bribes occured this round, stop
        if bribe_occured == False:
            break

    # Check if we have the original queue
    desired_queue = list(range(1, len(q)+1))

    if q == desired_queue:
        print(sum(n_bribes))
    else:
        print("Too chaotic")


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
