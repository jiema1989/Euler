# this file will return true or false, depending on whether the input is prime or not #
import math;
def main(n):
    if n==1:
        return False;
    if n==2:
        return True;
    elif n%2==0:
        return False;
    else:
        root_n = math.ceil(math.sqrt(n))+1;
        for i in xrange(3, int(root_n),2):
            if n%i == 0:
                return False;
                break;
        else:
            return True
