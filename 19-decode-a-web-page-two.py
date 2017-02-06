#! /bin/python3

import requests
import bs4 as bs

base_url = 'http://www.vanityfair.com/style/society/2014/06/mounica-lewinsky-humiliation-culture'
r = requests.get(base_url)
soup = bs.BeautifulSoup(r.text, 'html.parser')

for i in soup.find_all('div', {'id':'react-app'}):
    print (i)

