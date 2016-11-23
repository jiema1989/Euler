# Euler 9 ##

import math;
N=1000;
xLimit=math.ceil(math.floor(N/3));

for a in range(int(xLimit)):
    for b in range(int(xLimit)):
        if a**2+b**2==(1000-a-b)**2:
            print a,b,1000-a-b, a*b*(1000-a-b)
            break;
        else:
            b+=1;
        a+=1;



