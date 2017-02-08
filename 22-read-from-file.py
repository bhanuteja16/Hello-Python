#! /bin/python3

import requests

r = requests.get("http://www.practicepython.org/assets/Training_01.txt")
table = {}
for line in r.text.splitlines() :
    lst = line.split("/")
    if lst[2] in table :
        table[lst[2]] += 1
    else :
        table[lst[2]] = 1
print (table)
