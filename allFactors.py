 ## this file is used to generate all the factors for a number N ##
import math;

def main(n):
    data  = [];
    for i in xrange(1,n,1):
        if n % i == 0:
            data.append(i)
    return data


