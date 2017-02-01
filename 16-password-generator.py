#! /bin/python3

from random import randint

def password() :
    pw = ""
    length = randint(6,12)
    seed = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()bcdefghijklmnopqrstuvwxyz"
    for i in range(length):
        pw = pw + seed[randint(0,len(seed) - 1)]
    return pw

print ("Generating a random password")
print (password())



