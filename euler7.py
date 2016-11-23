# Euler Prolem 7 #
import math
N=10001;

def isPrime(x):
    xRoot=int(math.ceil(math.sqrt(x)))+1;
    for i in xrange(3,xRoot, 2):
        if x%i==0:
            return False
            break
    else:
        return True

def Findit(N):
    Num=3;
    count=2;
    while count<N:
        Num+=2;
        if isPrime(Num):
            count=count+1;
    return Num

print Findit(N)
        
