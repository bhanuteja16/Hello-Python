#!/bin/python3

def revstr(st):
    strlst = st.split(" ")
    revlst = strlst[::-1]
    return " ".join(revlst)

st = str(input("Enter the string: "))
print (revstr(st))
