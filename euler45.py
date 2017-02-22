# euler 45 #
N = 100000;
tri_list = [int(n*(n+1)/2) for n in range(N)];
pen_list = [int(n*(3*n-1)/2) for n in range(N)];
hex_list = [int(n*(2*n-1)) for n in range(N)];

tri_set = set(tri_list);
pen_set = set(pen_list);
hex_set = set(hex_list);

result = (tri_set.intersection(pen_set)).intersection(hex_set);

print (result)



