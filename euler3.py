# This Is To Solve The Largest Factor Problem ##
import math;
N=600851475143;

def factor(n):
    i=2;
    s=[];
    while i*i<=n:
        while n % i ==0:
            n = n/i;
            s.append(i);
        i=i+1;

    if n>1:
        s.append(n);
    return s

print factor(N);
