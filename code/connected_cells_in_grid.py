'''
https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem
'''

import math
import os
import random
import re
import sys


# Complete the connectedCell function below.
def connectedCell(matrix):
    n_rows = len(matrix)
    n_columns = len(matrix[0])

#   print_matrix(matrix)

    biggest_island = 0

    for i in range(n_rows):
        for j in range(n_columns):
            new_island = recursive_dfs(matrix, i, j)
            if new_island > biggest_island:
                biggest_island = new_island

    return biggest_island


def recursive_dfs(matrix, i, j):
    '''
    DFS to find size on an island in matrix.
    Will change matrix in-place!

    Parameters:
    -----------
    matrix: list
        List of lists containing grid.

    i: int
        Initial index for row to start search
        from.

    j: int
        Initial index for column to start search
        from.
    '''
    n_rows = len(matrix)
    n_columns = len(matrix[0])

    # If out of grid, return 0
    if i < 0 or j < 0 or i >= n_rows or j >= n_columns:
        return 0

    # Debug code
    #print_matrix(matrix)
    #print()
    #print(i, j)

    # If island available
    if matrix[i][j] == 1:
        # Sink the island
        matrix[i][j] = 0

        # Find more neighbouring islands
        return 1 + recursive_dfs(matrix, i, j-1) + recursive_dfs(matrix, i, j+1) + recursive_dfs(matrix, i+1, j+1) + recursive_dfs(matrix, i+1, j) + recursive_dfs(matrix, i+1, j-1) + recursive_dfs(matrix, i-1, j+1) + recursive_dfs(matrix, i-1, j) + recursive_dfs(matrix, i-1, j-1)

    else:
        # If no island found, return 0
        return 0


def print_matrix(matrix):
    '''
    Prints out matrix.
    '''
    print("")
    for i in range(len(matrix)):
        print("")
        for j in range(len(matrix[0])):
            print("{} ".format(matrix[i][j]) , end = '')




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
