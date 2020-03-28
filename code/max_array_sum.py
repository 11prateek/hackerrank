'''
https://www.hackerrank.com/challenges/max-array-sum/problem
'''

import math
import os
import random
import re
import sys


# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    """
    Use dynamic programming to find largest sum
    of non-adjacent elements.

    Parameters:
    -----------
    arr: list
    """
    largest_sum_arr = [arr[0], max(arr[0], arr[1])]

    for i in range(2, n):
       largest_sum_arr.append(
                    max(arr[i], arr[i] + largest_sum_arr[i-2], largest_sum_arr[i-1])
        )

    return largest_sum_arr[-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
