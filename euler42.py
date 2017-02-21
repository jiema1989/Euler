# euler 42 #

original_data = open("p42.txt","r");
data = [];
print original_data;
word = "";


for item in original_data:
    for string in item:
        if string != ",":
            if string != '"':
                word = word + string;
        if string == ",":    
            data.append(word)
            word = '';

def strConvertNum(x):
    num = ord(x)-64;
    return num;

word_sums = []

for word in data:
    number_list = [];
    for letter in word:
        if letter != "'":
            number_list.append(strConvertNum(letter))
    word_sums.append(sum(number_list))

print "the largest in word_sums is " + str(max(word_sums))


def triNumbers():
    tri_num_list = [];
    for i in range(1,30,1):
        tri_number = float(0.5*i*(i+1));
        tri_num_list.append(int(tri_number))
    return tri_num_list

def howMany():
    count = 0;
    for word_sum in word_sums:
        if word_sum in triNumbers():
            count += 1;
    return count


print howMany()



        


