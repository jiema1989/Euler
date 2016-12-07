# Euler Problem 483 ##
# Method 1 ###
import itertools as it


def dictConsturction(N):
    dict=[];
       
    return
a=[100,101,102]
a.pop()
print a


def listGenerator(choices,N,s):
    key = 5-len(choices);
    for value in choices:
        print "choices is ", choices
        print "key is ", key;
        print "value is", value
        s[key]=value;
        choices.pop(value-1);
        print "choice is", choices
        print "N is ", N
        print "s is ", s

        listGenerator(choices,N-1,s);
    return s
            






print " try the listGenerator Function "
print listGenerator([1,2,3,4],4,{})
print " test ended "

print [1,2,3,4,5].pop(1)





i=1;
b={1:5,2:2,3:4,4:1,5:3}
while b!=c:
    i=i+1;
    for key,value in a.items():
        b[key] = a[b[key]]
    print b

print i
