#! /bin/python3

import requests
from bs4 import BeautifulSoup

filename = input("Enter the file name with extension, in which you want to svae story: ")

base_url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html.parser')
with open(filename, 'w') as f :
    for i in soup.find_all('p') :
        f.write(i.text)
        f.write('\n\n')
        

