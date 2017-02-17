# euler 20#



def factorial(n):
    return 1 if n <2 else n*factorial(n-1);

def sum_digits(number):
    return sum([int(num) for num in str(number)])

print sum_digits(factorial(100))
