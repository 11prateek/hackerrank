'''
https://www.hackerrank.com/challenges/pairs/problem
'''

import math
import os
import random
import re
import sys


# Complete the pairs function below.
def pairs(k, arr):
    count = 0

    # Store all numbers and their occurences in a dictionary
    store_targets = dict()
    for i in arr:
        store_targets.update(
                            {i: store_targets.get(i, 0) + 1}
        )

    # Find counts from dictionary for each element
    for i in arr:
        count = count + store_targets.get(i + k, 0)

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))
