import requests
from bs4 import BeautifulSoup

file = open("input.txt")

input1 = file.read()

a = input1.split()

start_year = int(a[1])
end_year = int(a[3])
author = []

for i in range(4, len(a)):
    author.append(a[i])

URL = "http://explosm.net/comics/archive/2018/12/dave"

r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
'''
table = soup.findAll('img', attrs={'id': 'main-comic'})
print("------------")
for i in table:
    print(i['src'])

print("---------")
print(table)

print("------------")

'''


def find_num(img):
    s = ""
    k = 0
    for i in range(0,len(img)):
        if img[i] == '/':
            k = k + 1
        if img[i] == '/' and k == 2:
            i = i + 1
            while img[i] != '/':
                s = s + img[i]
                i = i + 1
            return s
            break


def con_month(month):
    if month == "December":
        x = 12
    elif month == "November":
        x = 11
    elif month == "October":
        x = 10
    elif month == "September":
        x = 9
    elif month == "August":
        x = 8
    elif month == "July":
        x = 7
    elif month == "June":
        x = 6
    elif month == "May":
        x = 5
    elif month == "April":
        x = 4
    elif month == "March":
        x = 3
    elif month == "February":
        x = 2
    else:
        x = 1
    return x


def convert(month, year, author):
    link = "http://explosm.net/comics/archive/"
    link = link + str(year)
    link = link + "/" + str(month) + "/"
    link = link + author
    return link


start_month = con_month(a[0])
end_month = con_month(a[2])
# print(start_month, end_month)
end_month = end_month + 1
if end_month > 12:
    end_month = end_month % 12
    end_year = end_year + 1
# print(start_month, end_month)
while start_month != end_month and start_year != end_year:
    for i in author:
        # print(i)
        link1 = convert(start_month, start_year, i)
        # print(link1)
        r1 = requests.get(link1)
        soup1 = BeautifulSoup(r1.content, 'html5lib')
        table1 = soup1.findAll('div', attrs={'class': 'small-3 medium-3 large-3 columns'})
        d = []
        p = []
        for j in table1:
            d.append(find_num(j.a['href']))
        # print(d)
        for j in d:
            link2 = "http://explosm.net/comics/" + j + "/"
            # print(link2)
            r2 = requests.get(link2)
            soup2 = BeautifulSoup(r2.content, 'html5lib')
            table2 = soup2.findAll('img', attrs={'id': 'main-comic'})
            # print(table2)
            for k in table2:
                p.append(k['src'])
        print(p)
    start_month = start_month + 1
    if start_month > 12:
        start_month = start_month % 12
        start_year = start_year + 1


# print(soup.prettify())



