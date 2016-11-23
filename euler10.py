# Euler Problem 10 ##
import math;
def isPrime(x):
    xRoot=math.ceil(math.sqrt(x))+1;
    for i in range(2,int(xRoot),1):
        if x%i==0:
            return False;
            break;
    else:
        return True; 


def ProdOfPrimes(N):
    i=3;
    sum=5;
    while i<N:
        i+=2;
        if isPrime(i):
            sum+=i;
    return sum        




N=2000000;
print ProdOfPrimes(N)
        
