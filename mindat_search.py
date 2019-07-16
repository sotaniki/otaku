from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import sys
import os
import urllib
import csv
import pprint

mineral = input("mineral name: ") #鉱物名を入れる　地域名とかでも行けるはず(地域名の場合重複してcsvに書き込む恐れがある)
url = "https://www.mindat.org/search.php?search=" + mineral #検索url
parent = "https://www.mindat.org"
html = urllib.request.urlopen(url) #指定したURLからhtmlをもってくる
soup = BeautifulSoup(html, 'html.parser')

a = soup.find_all('a') #<a>タグで囲まれた部分の中身を抜き出す
url_list = []
locality = []
num = 0

for tag in a:
    letter = "".join(str(tag)) #aタグの中身を文字列にする
    #print(letter)
    y = letter[9] + letter[10] + letter[11] + letter[12]
    #print(y)
    if y == "/loc": #aタグの中身の指定した箇所が/locに一致する場合、urlを取得
        for i in range(14):
            if letter[13+i] != '"': #urlを取得した後for文を抜ける
                y = y + letter[13+i]
            else:
                break
        url_list.append(parent + y)

        for item in tag: #産地名を持ってくる
            num = num + 1
            locality.append(item)
            print(item, parent+y) #ターミナル上に産地名とURLを表示

print(num) #the number of localities

filename = mineral + "_locality.csv" #csvファイルへの書き込み
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
