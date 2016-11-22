# This Is TO Solve Euler Project Problem 4 #
import math;
upperBound=997;
lowerBound=100;
s=[1];
for i in range(upperBound, lowerBound, -1):
    TestNumber=i*1000+int(str(i)[2])*100+int(str(i)[1])*10+int(str(i)[0])*1;
    TestNumberRoot=math.ceil(math.sqrt(TestNumber));
    for j in range(100,int(TestNumberRoot),1):
        if TestNumber%j==0:
            if len(str(j))==3 and len(str(TestNumber/j))==3:
                print TestNumber, j, TestNumber/j;






