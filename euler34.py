# euler 34 #
N = 1000000;

def factorial(n):
    return 1 if n <2 else n*factorial(n-1);

def num_check(n):
    return True if sum([factorial(int(i)) for i in str(n)]) == n else False;

print (sum(list(filter(num_check, range(3,N)))));