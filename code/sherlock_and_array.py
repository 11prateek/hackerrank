'''
https://www.hackerrank.com/challenges/sherlock-and-array/problem
'''


import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
    # Add all elements
    right_sum = sum(arr)
    left_sum = 0

    # Remove and check each element
    for i in arr:
        right_sum = right_sum - i
        print(left_sum, right_sum)
        if left_sum == right_sum:
            return "YES"

        left_sum = left_sum + i

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
