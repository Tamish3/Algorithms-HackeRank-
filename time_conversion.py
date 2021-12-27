#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    a = ''
    if s[-2:] == 'AM':
        if s[0:2] == '12':
            a = "{hour}{rest}".format(hour="00",rest=s[2:8])
        else:
            a = s[0:8]
    else:
        if s[0:2] != '12':
            a = "{hour}{rest}".format(hour=str(int(s[0:2]) + 12),rest=s[2:8])
        else:
            a = s[0:8]
    return a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
