# Euler 6 ##

N=100;

def function1(N):
    sum1=0;
    for i in range(0,N+1,1):
        sum1+=i;
    return sum1**2;
def function2(N):
    sum2=0
    for i in range(0,N+1,1):
        sum2+=i**2;
    return sum2;

print function1(N)-function2(N);

