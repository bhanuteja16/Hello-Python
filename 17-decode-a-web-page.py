#! /bin/python3

import requests
import bs4 as bs

url = "https://www.nytimes.com"
r = requests.get(url)
soup = bs.BeautifulSoup(r.text, 'html.parser')


for tag in soup.find_all('article', {"class" : "story"}) :
    #print (tag)
    n = tag.findNext('h2', {"class" : "story-heading"})
    #print (n)
    print (n.findNext('a').text)
    #print ("============================================================================")
