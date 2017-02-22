# Euler 43 #
import itertools;
from copy import deepcopy;


def num_check(n):
	n_str = str(n);
	numbers = [int(n_str[i]+n_str[i+1]+n_str[i+2]) for i in range(1, 8)];
	primes = [2,3,5,7,11,13,17];
	conditions = [numbers[i]%primes[i]==0 for i in range(7)];
	return all(conditions);
	
	
all_pan_num = deepcopy(itertools.permutations("1234567890", 10));
num_list = list(all_pan_num);
num_list = [''.join(item) for item in num_list];
result_set = list(filter(num_check, num_list));
result = sum([int(str_num) for str_num in result_set]);
print (result);



