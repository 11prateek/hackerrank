"""
https://www.hackerrank.com/challenges/queens-attack-2/problem
"""

import math
import os
import random
import re
import sys


# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):

    hash_obstacles = {}
    print(obstacles)
    for o in obstacles:
        hash_obstacles["{}_{}".format(o[0], o[1])] = -1

    print(hash_obstacles)

    total = 0

    # Search up
    for i in range(r_q+1, n+1):
        j = c_q
        if hash_obstacles.get("{}_{}".format(i, j), 0) < 0:
            break
        print(i,j)
        total = total + 1

    # Search down
    for i in range(r_q-1, 0, -1):
        j = c_q
        if hash_obstacles.get("{}_{}".format(i, j), 0) < 0:
            break
        print(i,j)
        total = total + 1

   # Search left
    for j in range(c_q-1, 0, -1):
        i = r_q
        if hash_obstacles.get("{}_{}".format(i, j), 0) < 0:
            break
        print(i,j)
        total = total + 1

    # Search right
    for j in range(c_q+1, n+1):
        i = r_q
        if hash_obstacles.get("{}_{}".format(i, j), 0) < 0:
            break
        print(i,j)
        total = total + 1

    # Search right-diagonal up
    for i, j in zip(range(r_q+1, n+1, 1), range(c_q+1, n+1, 1)):
        if hash_obstacles.get("{}_{}".format(i, j), 0) < 0:
            break
        print(i,j)
        total = total + 1

    # Search left-diagonal up
    for i, j in zip(range(r_q+1, n+1, 1), range(c_q-1, 0, -1)):
        if hash_obstacles.get("{}_{}".format(i, j), 0) < 0:
            break
        print(i,j)
        total = total + 1

    # Search right-diagonal down
    for i, j in zip(range(r_q-1, 0, -1), range(c_q+1, n+1, 1)):
        if hash_obstacles.get("{}_{}".format(i, j), 0) < 0:
            break
        print(i,j)
        total = total + 1

    # Search left-diagonal down
    for i, j in zip(range(r_q-1, 0, -1), range(c_q-1, 0, -1)):
        if hash_obstacles.get("{}_{}".format(i, j), 0) < 0:
            break
        print(i,j)
        total = total + 1

    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
