#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    length = 0
    pos = 0
    neg = 0
    zero = 0

    for x in arr:
        length += 1
        if x > 0:
            pos += 1
        elif x < 0:
            neg += 1
        else:
            zero += 1

    print(round(pos/length,6))
    print(round(neg/length,6))
    print(round(zero/length,6))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
