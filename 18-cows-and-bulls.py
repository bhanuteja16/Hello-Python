#! /bin/python3

from random import randint

print ("Welcome to the Cows and Bulls Game !")

orglst = [int(i) for i in str(randint(1111,9999))]
print (orglst)
count = 0

while True :
    num = int(input("Enter a four digit number: "))
    if num >= 9999 or num <= 1111 :
        print ("Invalid input")
        exit()
    numlst = [int(i) for i in str(num)]
    #print (numlst)
    cows = 0
    bulls = 0
    count = count  + 1
    tmplst = orglst 
    # for cows
    for i in range(len(tmplst)) :
        if tmplst[i] == numlst[i]:
            cows = cows + 1
            tmplst[i] = 'X'
            numlst[i] = 'x'
    # for bulls
    for i in numlst :
        if i in tmplst :
            bulls = bulls + 1

    if numlst == ['x', 'x', 'x' ,'x'] :
        print ("you have found all the cows") 
        break 
    else :
        print ("you have found " + str(cows) + " Cows and " + str(bulls) + " bulls. Try again ..")

print ("you have made " + str(count) + " guess")

