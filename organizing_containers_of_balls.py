'''
https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem
'''

import math
import os
import random
import re
import sys


# Complete the organizingContainers function below.
def organizingContainers(container):
    n_balls_per_container = [sum(x) for x in container]
    n_balls_per_color = {}

    for cont in container:
        for i in range(len(container)):
            n_balls_per_color[i] = n_balls_per_color.get(i, 0) + cont[i]

    n_balls_per_color = list(n_balls_per_color.values())

    n_balls_per_container.sort()
    n_balls_per_color.sort()

    if n_balls_per_container != n_balls_per_color:
        return "Impossible"
    else:
        return "Possible"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
