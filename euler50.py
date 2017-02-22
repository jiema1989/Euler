## euler 50 ##

import math;
from isprime import main as isma;
from primeGenerator import main as gema;

N = 1000000;
def consecutive_gen():
	set_of_primes = gema(N);
	all_possible_consecutive = [];
	for i in range(len(set_of_primes)-1):
		j = i;
		max_length_seq = [];
		sum = 0;
		while sum < N:
			j+=1;
			sum += set_of_primes[j-1];
			max_length_seq.append(set_of_primes[j-1]);	
		all_possible_consecutive.append(max_length_seq[:-1]);
	return all_possible_consecutive;

	
def consecutive_sum(somelist):
	all_primes_sums_list = [];
	for each_sub_list in somelist:
		sums = [sum(each_sub_list[0:j]) for j in range(1, len(each_sub_list)+1)];
		sums_are_primes = [isma(sum) for sum in sums];
		to_return = [[each_sub_list[0], (j+1), sums[j]] for j in range(len(each_sub_list)) if sums_are_primes[j] == True];
		all_primes_sums_list+=to_return;
	return all_primes_sums_list;
	

def greatest_consecutive_pick(alist):
	length_of_seq = max([v2 for v1,v2,v3 in alist]);
	return [v3 for v1,v2,v3 in alist if v2 == length_of_seq];

print (consecutive_sum(consecutive_gen()));
print (greatest_consecutive_pick(consecutive_sum(consecutive_gen())));
		
		
		
		
		
		
		
	
	






