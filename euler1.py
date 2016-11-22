# This is used to solve Euler Problem 1#
def euler(number):
    sum=0;
    for i in xrange(number+1):
        if i%3==0 or i%5==0:
            sum+=i;
    return sum;
print euler(1000);
