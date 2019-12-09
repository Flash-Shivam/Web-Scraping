import requests
from bs4 import BeautifulSoup

URL = "https://github.com/ShouryaAggarwal"

'''
print(r.status_code)
if r.status_code == 200:
    print("success")
else:
    print("failure")

r.encoding = 'utf-8'
'''

r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

table = soup.findAll('span', attrs={'class': 'repo'})
print("------------")
for i in table:
    print(i.text)

# print(table)

print("------------")
