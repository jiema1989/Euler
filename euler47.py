# euler 47#
import math;
iteration = 4;


def decompose(n):
    dataDic={};
    root_n = math.ceil(math.sqrt(n))+1;
    if n%2 ==0:
        dataDic[2]=0;
        while n%2==0:
            n = n/2;
            dataDic[2] = dataDic[2]+1;

    for i in xrange(3,int(root_n),2):
        if n %i ==0:
            dataDic[i]=0;
            while n%i == 0:
                n = n/i;
                dataDic[i] = dataDic[i]+1
    if n>1:
        dataDic[n] = 1;
    return dataDic
 
def justify(N):
    j=0;
    while len(decompose(N))==iteration:
        N = N+1;
        j = j+1;
        justify(N)
    return j - iteration ==0

def main():
    num =3;
    while justify(num)==False:
        num += 1;
    return num



print main()
