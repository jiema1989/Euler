# euler 50 #

import isprime;
import primeGenerator;
import math;

N = 1000000;
threshold = 1000000;
data = [1] + primeGenerator.main(N);

def main(data):
    dict = {};
    length = len(data);
    sum = 0;
    for i in range(length):
        if sum > threshold:
            break;
        else:
            sum += data[i];
            if isprime.main(sum):
                dict[i+1] = sum
    return dict


def iter():
    maxCom = {0:0};
    while len(data)!=0:
        del data[0];
        result = main(data);
        result_num = max([x for x in result.keys()]);
        result_sum = result[result_num];
        if result_num > maxCom.keys()[0]:
            maxCom.clear();
            maxCom[result_num] = result_sum;
    return maxCom


print iter()
