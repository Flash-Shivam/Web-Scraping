import os

x = os.getcwd()

os.makedirs("2019")
os.chdir("2019")
os.makedirs("Jan")
os.chdir(x)

os.makedirs("2017")
