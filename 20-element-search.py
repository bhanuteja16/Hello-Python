#! /bin/python3
from random import randint

def binarysearch(lst, num) :
    b = len(lst) - 1
    a = b // 2
    if a == 0 and lst[a] != num :
        print ("Number does not exist")
        exit()
    if lst[a] < num :
        binarysearch(lst[a:b], num)
    elif lst[a] > num :
        binarysearch(lst[0:a], num)
    elif lst[a] == num :
        print ("Number exists in the list")

def randlist() :
    l = randint(5,8)
    lst = []
    for i in range(l):
        lst.append (randint(0,9))
    lst.sort()    
    return lst

lst = randlist()
print (lst)
num = int(input("Enter the Number: "))
binarysearch(lst,num)
