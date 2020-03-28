'''
https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem
'''

import math
import os
import random
import re
import sys


# Complete the stepPerms function below.
def stepPerms(n, cache):
    '''
    Memoised 3-step Fibonacci.
    '''
    if n in cache:
        return cache[n]
    else:
        cache[n] = stepPerms(n - 3, cache) +  stepPerms(n - 2, cache) + stepPerms(n - 1, cache)
    return cache[n]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n, cache={1:1, 2:2, 3:4})

        fptr.write(str(res) + '\n')

    fptr.close()
