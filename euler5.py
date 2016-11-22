## Euler Problem 5 ##
N=20;

def factorNum(n):
    s={};
    i=2;
    exp=0;
    while i*i<=n:
        while n%i==0:
            exp+=1;
            n=n/i;
            s[i]=exp;
        i=i+1;
        exp=0;
    if n>1:
        s[n]=1;
    return s;

print factorNum(20)

dictEntire={};

for i in range(2,20,1):
    dict2 = factorNum(i);
    for factor in dict2.keys():
        if factor not in dictEntire:
            dictEntire[factor]=1;
        if factor in dictEntire:
            if dict2[factor]>=dictEntire[factor]:
                dictEntire[factor]=dict2[factor];

print dictEntire

pro=1;
for key,value in dictEntire.items():
    pro=pro*(key**value);
print pro;
