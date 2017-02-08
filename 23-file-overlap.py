#! /bin/python3

import string

def readfile(a) :
    lines = a.readlines()
    lst = []
    for i in lines :
        num = int(i.replace('\n', ''))
        lst.append(num)
    return lst

f = open('primenumbers.txt', 'r')
g = open('happynumbers.txt', 'r')
lst1 = readfile(f)
lst2 = readfile(g)
f.close()
g.close()
c = [x for x in lst1 if x in lst2]
print (c)
