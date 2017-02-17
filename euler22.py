# euler 22#

f = open("p022_names.txt", "r");
word_data=[];


s = "";
print "type of s", type(s)
for data in f:
    for item in data:
        if item == '"':
            continue
        if item != ",":
            s  = s + item ;
        if item == ",":
            word_data.append(s);
            s = "";

print len(word_data)   
word_data.sort()

print word_data


count = 1;
sum_all = 0;
for name in word_data:
    value = sum([ord(letter)-64 for letter in name])*(count+1);
    count +=1;
    sum_all += value;

print sum_all


