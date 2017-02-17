# euler 21#
import math;
N = 10000;

def divisor(n):
    threshold = int(math.floor(math.sqrt(n)))+1;
    all_divisors = set([x for x in range(1,threshold) if n%x == 0] + [n/x for x in range(1,threshold) if n%x ==0]);
    return dict({n:sum(all_divisors)-n})


def whole_dict(N):
    entire_dict = {0:0,1:0};
    for n in range(2,N+1):
        entire_dict[n] = divisor(n)[n];
    return entire_dict;


def find_pairs(dictionary):
    selected_dict = {};
    all_values = [value for value in dictionary.values() if value < N+1];
    all_keys = [key for key in dictionary.keys()];
    for key in all_keys:
        if dictionary[key] in all_values:
            print key, dictionary[key]
            if dictionary[dictionary[key]] == key:
                if key != dictionary[key]:
                    selected_dict[key] = dictionary[key]
    return selected_dict


def sum_pairs(dictionary):
    return sum([key for key in dictionary.keys()])





entire_dict = whole_dict(N);

pairs = find_pairs(entire_dict);

print pairs
print sum_pairs(pairs)
