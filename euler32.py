# euler 32 #
import math;

number_list = list(range(1000,10000));

number_set = set("123456789");
         
def check_pan(n):
    cut  = int(math.ceil(math.sqrt(n))+1);
    for i in range(1,cut):
        if n % i ==0:
            i1 = str(i);
            i2 = str(int(n/i));
            i3 = str(n);
            str_combined = i1+i2+i3;
            if len(str_combined) == 9 and set(str_combined) == number_set:
                return True;
    else:
        return False;

print (sum([n * check_pan(n) for n in number_list]))
print (list(filter(check_pan, number_list)))         
