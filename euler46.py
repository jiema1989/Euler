# euler 46 #
import math;

def decompose(n):
    all_primes = allPrimeUpTo(n);
    for prime in all_primes:
        u = (n - prime)/2;
        if math.sqrt(u) == math.floor(math.sqrt(u)):
            return False
            break
    else:
        print "we find one!, which is:"
        print n
        return True


def prime(n):
    if n%2==0:
        return False;
    else:
        root_n = math.ceil(math.sqrt(n))+1;
        for i in xrange(3,int(root_n),2):
            if n%i ==0:
                return False
                break
        else:
            return True

def allPrimeUpTo(N):
    data = [];
    for i in range(3,N+1, 2):
        if prime(i):
            data.append(i)
    return data

def main():
    n = 3;
    while decompose(n)==False:
        n += 2;
    return n

main()
            
    
