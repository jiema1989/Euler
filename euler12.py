#Euler Problem 12#
import math
def SumGenerator(N):
    sum=0;
    for i in range(N+1):
        sum+=i;
    return sum

def factorExt(x):
    s={};
    xRoot=math.ceil(math.sqrt(x))+1;
    for i in range(2,int(xRoot),1):
        if x%i==0:
            s[i]=0;
            while not x%i:
                x=x/i;
                s[i]+=1;
    if x>1:
        s[x]=1;
    return s


def factorPro(s):
    prod = 1;
    for i,j in s.items():
        prod = prod*(j+1);
    return prod


def factorNum(s):
    return len(s)

def MainResult(N):
    i=1;
    l=0;
    while l<=N:
        i+=1;
        y = SumGenerator(i);
        s = factorExt(y);
        l = factorPro(s);
    return y; 
N=500;
print MainResult(N)

    
