#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#


def getMax(operations):
    # Write your code here
    ans = []
    stk = []
    mx = -1
    for i in operations:
        op = list(map(int, i.split()))
        if len(op) == 2:
            mx = max(mx, op[1])
            stk.insert(0, mx)
        elif op[0] == 2:
            #print('in 2')
            x = stk.pop(0)
            if stk:
                mx = stk[0]
            else:
                mx = -1

        elif op[0] == 3:
            if stk:
                ans += [stk[0]]

            # print(stk)

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
