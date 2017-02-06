#! /bin/python3

import requests
from bs4 import BeautifulSoup
 
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html.parser')
 
for story_heading in soup.find_all(class_="story-heading"): 
    #print (story_heading)
    #print ("---------------------------------------------------------")
    if story_heading.a :
        print (story_heading.a.text.strip())
    else :
        print (story_heading.text.strip())
