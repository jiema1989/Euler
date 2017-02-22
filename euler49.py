 ### euler49 ###
import math;
import itertools as it;
from copy import deepcopy;
from isprime import main as ma;
 
def all_permu(n):
	all_permutations = deepcopy(it.permutations(str(n), 4));
	all_permutations = set([int(''.join(permutation)) for permutation in all_permutations]);
	return all_permutations;
	
def primes_check(someset):
	checks = sorted([number for number in someset if ma(number) == True]);
	differences = [];
	N = len(checks);
	for i in range(N):
		for j in range(i,N):
			differences.append([i,j,checks[j] - checks[i]]);
	len_diff = len(differences);
	for index1 in range(len_diff):
		i1,j1,diff1 = differences[index1];
		for index2 in range(index1+1, len_diff):
			i2,j2,diff2 = differences[index2];
			if j1 == i2 and diff1 == diff2:
				return [checks[i1], checks[j1], checks[j2]];
	else:
		return []
				
four_digits_numbers = [i for i in range(1000,10000)];
four_digits_permutations = [all_permu(num) for num in four_digits_numbers];
checks = [primes_check(permutation) for permutation in four_digits_permutations if len(primes_check(permutation))!=0];

print (checks);
