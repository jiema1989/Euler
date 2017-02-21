# euler 33 #

def fract(m,n):
    if str(n)[1]=="0" or str(m)[0] == str(m)[1]:
        return False;
    else:
        return True if (m+.0)/n == (int(str(m)[0])+.0)/ int((str(n)[1])) and str(m)[1] == str(n)[0] else False

result = [[m,n] for m in range(10,100) for n in range (10,100) if fract(m,n)];
print (result)
def divi(list_var):
    m = list_var[0];
    n = list_var[1];
    for i in range(2,m+1):
        if m % i ==0 and n % i == 0:
            while m % i ==0 and n % i ==0:
                m = m/i;
                n = n/i;
    return [int(m),int(n)]

numer, denom = 1,1;
for i in range(len(result)):
    numer *= result[i][0];
    denom *= result[i][1];
                   
print (divi([numer, denom]))

          