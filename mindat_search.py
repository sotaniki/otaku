from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import sys
import os
import urllib
import csv
import pprint

mineral = input("mineral name: ") #鉱物名を入れてね　地域名とかでも行けるはず
url = "https://www.mindat.org/search.php?search=" + mineral
parent = "https://www.mindat.org"
html = urllib.request.urlopen(url) #指定したURLからhtmlをもってくる
soup = BeautifulSoup(html, 'html.parser')

a = soup.find_all('a') #<a>タグで囲まれた部分の中身を抜き出す
url_list = []
locality = []
num = 0

for tag in a:
    mojiretsu = ','.join(str(tag)) #tagが扱いづらい型なので文字列化した
    s = mojiretsu[18] + mojiretsu[20] + mojiretsu[22] + mojiretsu[24]
    if s == "/loc":
        for i in range(14):
            if mojiretsu[22+i*2] != '"':
                s = s + mojiretsu[22+i*2]
            else:
                break
        url_list.append(parent + s)
        for item in tag: #産地名を持ってくる
            num = num + 1
            locality.append(item)

print(num) #the number of localities

filename = mineral + "_locality.csv"
g = open(filename, 'w')
writer = csv.writer(g, lineterminator='\n')
csvlist = []
csvlist.append("locality")
csvlist.append("url")
writer.writerow(csvlist)

for i in range(num):
    csvlist = []
    csvlist.append(locality[i])
    csvlist.append(url_list[i])
    writer.writerow(csvlist)

g.close()
