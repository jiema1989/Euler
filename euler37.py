# euler 37 #

import isprime;

def truncation(n):
    while isprime.main(n) == True:
        remainder = (n - n/10*10);
        n = (n-remainder)/10;
        truncation(n)
    if n==0:
        return True
    else:
        return False


def cut(n):
    while isprime.main(n) ==True:
        n_string = str(n);
        first_digit = n_string[0];
        n = n - int(first_digit) * (10**(len(str(n))-1));
        cut(n)
    if n ==0:
        return True
    else:
        return False


def main():
    n = 11;
    count = 0;
    data = [];
    while count<11:
        n += 1;
        if cut(n) and truncation(n):
            count +=1;
            data.append(n)
    return data, sum(data)

print main()

