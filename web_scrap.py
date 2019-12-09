import requests
import os
from bs4 import BeautifulSoup

# print(os.getcwd())

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


def con_month1(x):
    if x == 1:
        return "January"
    if x == 2:
        return "February"
    if x == 3:
        return "March"
    if x == 4:
        return "April"
    if x == 5:
        return "May"
    if x == 6:
        return "June"
    if x == 7:
        return "July"
    if x == 8:
        return "August"
    if x == 9:
        return "September"
    if x == 10:
        return "October"
    if x == 11:
        return "November"
    return "December"


def convert(month, year, author):
    link = "http://explosm.net/comics/archive/"
    link = link + str(year)
    link = link + "/" + str(month) + "/"
    link = link + author
    return link


def file_name(date, author):
    x = ""
    x = x + date + "-" + author + ".png"
    return x


def con_date(text):
    # print(text, len(text))
    k = 0
    x = ""
    for i in range(0, len(text)):
        if text[i] == '.':
            k = k + 1
        if k == 2:
            # print(i)
            i = i + 1
            x = x + text[i] + text[i+1]
            # print(x)
            return x


def date_sel(month, year, date):
    x = ""
    x = x + str(year) + "." + str(month) + "." + date
    return x


start_month = con_month(a[0])
end_month = con_month(a[2])
# print(start_month, end_month)
end_month = end_month + 1
if end_month > 12:
    end_month = end_month % 12
    end_year = end_year + 1
p = []

current_path = os.getcwd()

os.makedirs(str(start_year))

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
        for j in table1:
            d.append(find_num(j.a['href']))
        # print
        p = []
        z = []
        for j in d:
            link2 = "http://explosm.net/comics/" + j + "/"
            # print(link2)
            r2 = requests.get(link2)
            soup2 = BeautifulSoup(r2.content, 'html5lib')
            table2 = soup2.findAll('img', attrs={'id': 'main-comic'})
            table3 = soup2.findAll('div', attrs={'id': 'comic-info-text'})
            # print(table2)
            for k in table2:
                p.append(k['src'])
            for k in table3:
                z.append(date_sel(start_month,start_year,con_date(k.find('div', attrs={'id': 'comic-author'}).text)))
        # print(p)
        # print(z)

    os.chdir(str(start_year))
    os.makedirs(con_month1(start_month))
    os.chdir(con_month1(start_month))
    
    for j in range(0, len(p)):
        r3 = requests.get("http:" + p[j])
        with open(file_name(z[j], i), 'wb') as f:
            f.write(r3.content)
    os.chdir(current_path)

    start_month = start_month + 1
    if start_month > 12:
        start_month = start_month % 12
        os.chdir(current_path)
        start_year = start_year + 1
        os.makedirs(str(start_year))
    # print(soup.prettify())



