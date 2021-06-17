import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#


def arrayManipulation(n, queries):
    # Write your code here
    arr = [0]*n
    print("len", len(arr))
    for q in queries:
        i, j, k = map(int, q)
        # print(i-1,j-1,k)
        #print("test", arr[i-1], arr[j-1], arr[j-1] - k)
        arr[i-1] += k
        if j < n:
            arr[j] -= k

    add = 0
    mx = -1
    for i in range(n):
        arr[i] += add
        add = arr[i]
        if mx < arr[i]:
            mx = arr[i]
    #test_arr = [0]*n
    # for q in queries:
    #    i,j,k = map(int, q)
    #    for x in range(i-1,j):
    #         test_arr[x] += k

    # print(*arr)
    # print(*test_arr)
    return mx


if __name__ == '__main__':
    fptr = open('output.txt', 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
