# Euler 2: Fibonacci Problem #
def euler2():
    sumout=2;
    s=[1,2];
    while isGreaterThan4m(s[-1]+s[-2]):
        y = s[-1]+s[-2];
        s.append(y);
        sumout += y * int(y%2==0);
    return sumout;
def isGreaterThan4m(x):
    return x<=4000000;
print euler2();
