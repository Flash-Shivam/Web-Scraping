import os
import requests
from bs4 import BeautifulSoup

x = os.getcwd()

URL = "http://explosm.net/rcg"

r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

table = soup.findAll('img', attrs={'alt': ''})

p = []
p.append(table[1]['src'])
p.append(table[2]['src'])
p.append(table[3]['src'])

os.makedirs("random")
os.chdir("random")
for i in range(0, len(p)):
    r3 = requests.get(p[i])
    with open("frame" + str(i+1) + ".png", 'wb') as f:
        f.write(r3.content)
os.chdir(x)


