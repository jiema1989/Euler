# euler 48 #
N = 1000;

def main(N):
    sum = 0;
    for i in xrange(1,N+1,1):
        sum += i**i;
    return sum



print main(N)
