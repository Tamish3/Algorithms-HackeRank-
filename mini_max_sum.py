#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    max = arr[0]
    min = arr[0]
    sum = 0
    for number in arr:
        sum += number
        if number < min:
            min = number
        elif number > max:
            max = number
    print("{} {}".format((sum-max), (sum-min)) )
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
