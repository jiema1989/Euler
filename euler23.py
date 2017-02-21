## euler 23 ##
import math
import allFactors as af

Number = 29000;


def sumFactors(N):
    data = af.main(N)
    return sum(data)


def isAbundant(N):
    if sumFactors(N) > N:
        return True;
    else:
        return False;

def abunNumGenerator(N):
    data = [];
    for i in range(1,N+1,1):
        if isAbundant(i):
            data.append(i)
    return data;


def abunSum(data1, data2):
    dataset = set();
    for item1 in data1:
        for item2 in data2:
            if item1+item2 <= 28123 and item1+item2 not in dataset:
                dataset.add( item1+item2)
    return dataset


def main(N):
    allNumSet = set([i for i in range(1,N+1,1)]);
    dataset_to_exclude = abunSum(abunNumGenerator(Number), abunNumGenerator(Number));
    resultSet = allNumSet - dataset_to_exclude;
    return sum(resultSet)


print "Generator gives"
print abunNumGenerator(Number)
print "-"*100
print "All numbers that is the sum of two abundants are"
print abunSum(abunNumGenerator(Number), abunNumGenerator(Number))
print "the sum of the remaining is"
print main(Number)


