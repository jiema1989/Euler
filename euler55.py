# euler 55 #

def reverse(x):
    x = str(x);
    y = '';
    while len(x)!=0:
        digit = x[-1];
        x = x[0:-1]
        y = y + digit;
    return int(y)


def isLychrel(x):
    num_sum = x + reverse(x);
    sum_str = str(num_sum);
    if len(sum_str)%2 == 0:
        pos = sum_str[0:len(sum_str)/2];
        neg = sum_str[len(sum_str)/2:];
        pos = int(pos)
        neg = int(neg)
        if pos == reverse(neg):
            return True;
        else:
            return False;
    if len(sum_str)%2 ==1:
        pos = sum_str[0:(len(sum_str)-1)/2];
        neg = sum_str[(len(sum_str)+1)/2:];
        pos = int(pos)
        neg = int(neg)
        if pos == reverse(neg):
            return True;
        else:
            return False;


def isIterLyn(x):
    if x == reverse(x):
        return True;
    else:
        for i in range(51):
            if isLychrel(x):
                return True;
                break;
            else:
                x = x + reverse(x);
        else:
            return False;


def lycheralList():
    data =[];
    for i in range(10,10001,1):
        print i, isIterLyn(i);
        if isIterLyn(i):
            data.append(i)
    data_set = set(data)
    entire_dataset = set([i for i in range(1,10001,1)])
    remaining_set = entire_dataset - data_set;
    return  len(data), remaining_set

print lycheralList()
