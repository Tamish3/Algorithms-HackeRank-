#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    result = [0] * 2
    counts = [0] * 2
    if scores is None:
        return [0,0]
    result[0] = scores[0]   # tracks max score
    result[1] = scores[0]   # tracks min score
    for score in scores[1:]:
        if result[0] < score:
            counts[0] += 1
            result[0] = score
        elif result[1] > score:
            counts[1] += 1
            result[1] = score

    return counts


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
