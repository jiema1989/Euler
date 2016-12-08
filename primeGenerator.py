# this file is used to generate prime numbers up to N #

import math;
import isprime;

def main(N):
    data = [];
    for i in range(2,N+1,1):
        if isprime.main(i):
            data.append(i)
    return data

