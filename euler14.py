# this is to solve euler 14 #

N = 1000000;
import math;


def count(N):
    bigStart = 1;
    big = 1;
    for n in xrange(2,N+1,1):
        m = n;
        print m;
        j =0;
        while n != 1:
            if n%2 ==0:
                n = n/2;
                j =  j + 1;
            else:
                n = 3*n + 1;
                j = j + 1;
        if j > big:
            big = j;
            bigStart = m;
    return bigStart, big


print count(N)

