# euler 16#

import math;

def sumNum(n):
    sum = 0;
    for digit in str(n):
        sum += float(digit);
    return sum


print sumNum(4**500)

