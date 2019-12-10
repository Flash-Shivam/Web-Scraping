import os
from datetime import date
import requests
from bs4 import BeautifulSoup

x = os.getcwd()

file = open("input.txt")
input1 = file.read()

a = input1.split()

number = int(a[1])

today = date.today()
p = str(today)
t = p.split('-')
start_year = int(t[0])
start_month = int(t[1])
start_month = start_month - 1
if start_month <= 0:
    start_month = 12
    start_year = start_year - 1

link1 = "http://explosm.net/comics/archive"
r = requests.get(link1)
soup = BeautifulSoup(r.content, 'html5lib')
k = 0

r1 = requests.get(link1)
soup1 = BeautifulSoup(r1.content, 'html5lib')
table1 = soup1.findAll('div', attrs={'class': 'small-3 medium-3 large-3 columns'})
d = []


def find_num(img):
    s = ""
    k = 0
    for i in range(0, len(img)):
        if img[i] == '/':
            k = k + 1
        if img[i] == '/' and k == 2:
            i = i + 1
            while img[i] != '/':
                s = s + img[i]
                i = i + 1
            return s
            break


for i in table1:
    d.append(find_num(i.a['href']))

while len(d) <= number:
    if start_month == 12:
        link = link1 + "/" + str(start_year)
    else:
        link = link1 + "/" + str(start_year) + "/" + str(start_month)
    # print(link)
    r2 = requests.get(link)
    soup2 = BeautifulSoup(r2.content, 'html5lib')
    table2 = soup2.findAll('div', attrs={'class': 'small-3 medium-3 large-3 columns'})
    for i in table2:
        d.append(find_num(i.a['href']))
    start_month = start_month - 1
    if start_month <= 0:
        start_month = 12
        start_year = start_year - 1

# print(len(d), d)


def con_date(text):
    # print(text, len(text))
    x = ""
    for i in range(1, 11):
        x = x + text[i]
    return x


def con_author(text):
    # print(text, len(text))
    # print(text[13],text[14],text[15])
    x = ""
    for i in range(15, len(text)):
        if text[i] == ' ':
            break
        x = x + text[i]
    return x


def file_name(date, author):
    x = ""
    x = x + date + "-" + author + ".png"
    return x


p = []
z = []
e = []
for j in d:
    link2 = "http://explosm.net/comics/" + j + "/"
    # print(link2)
    r3 = requests.get(link2)
    soup3 = BeautifulSoup(r3.content, 'html5lib')
    table3 = soup3.findAll('img', attrs={'id': 'main-comic'})
    table4 = soup3.findAll('div', attrs={'id': 'comic-info-text'})
    # print(table4)
    for k in table3:
        p.append(k['src'])
    for k in table4:
        z.append(con_date(k.find('div', attrs={'id': 'comic-author'}).text))
        e.append(con_author(k.find('div', attrs={'id': 'comic-author'}).text))

os.makedirs("latest")
os.chdir("latest")
for j in range(0, number):
    r4 = requests.get("http:" + p[j])
    with open(file_name(z[j], e[j]), 'wb') as f:
        f.write(r4.content)
