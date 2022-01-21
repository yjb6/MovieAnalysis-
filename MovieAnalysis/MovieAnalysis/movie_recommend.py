import re
import urllib.parse
import urllib.request
import numpy as np
import pandas as pd
import heapq
import re
import csv
import random
from time import sleep
import requests
import json
import string
import urllib.parse
from bs4 import BeautifulSoup


useragent = ['Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
             'Chrome/59.0.3102.62 Safari/537.36',
             'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
             'Chrome/60.0.3102.62 Safari/537.36',
             'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
             'Chrome/61.0.3102.62 Safari/537.36',
             'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
             'Chrome/62.0.3102.62 Safari/537.36',
             'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
             'Chrome/63.0.3102.62 Safari/537.36',
             'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
             'Chrome / 77.0.3865.90Safari / 537.36',
             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
             'Chrome/78.0.4472.124 Safari/537.36 ',
             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
             'Chrome/90.0.4472.124 Safari/537.36 ',
             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
             'Chrome/91.0.4472.124 Safari/537.36 ',
             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
             'Chrome/89.0.4472.124 Safari/537.36 '
             ]
def haibao(ID):
    url = 'https://www.imdb.com/title/tt'+ID+'/'

    headers = {
                    'User-Agent': random.choice(useragent)
    }
    data_json = requests.get(url, headers=headers).content.decode()
    soupData = BeautifulSoup(data_json, 'lxml')
    # print(soupData)
    aa=soupData.find(attrs={'property':'twitter:image'})
    A=str(aa).find('content=')
    B = str(aa).find('.jpg')
    return  str(aa)[A+9:B+4]

def getmovie(uid):
    movies = pd.read_csv(r"C:\MovieAnalysis\MovieAnalysis\MovieAnalysis\imdb.csv",dtype=str)
    names=pd.read_csv(r"C:\MovieAnalysis\MovieAnalysis\MovieAnalysis\recommend_name.csv")
    # print(movies.iloc[int(uid)])
    imdblist=[]
    name=[]
    p=[]
    for i in range(1,13):
        print(i)
        u="https://www.imdb.com/title/tt"+movies.iloc[int(uid)][i]+"/"
        p.append(haibao(movies.iloc[int(uid)][i]))
        imdblist.append(u)
    print(p)
    # for i in range(1,len(names.iloc[int(uid)])):
    #     name.append(names.iloc[int(uid)][i])
    # print(name)
    # picturelist=getpicurl(name)
    # print(picturelist)
    # print("______")
    # print(imdblist)
    r={"url":imdblist,"pic":p}
    return r


def getHtml(url):
    html=urllib.request.urlopen(url).read()
    return html
def getImg(html):
    A=html.find("thumbURL")
    B=html[A:].find(".jpg")
    return html[A+11:A+B+4]


def getname():
    pass
def getpicurl(list):
    # list = ['我不是药神', '你好，李焕英', '1921']
    urllist=[]
    for i in range(len(list)):
        data = urllib.parse.quote(list[i] + ' 海报')
        html = str(getHtml("http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=" + data))
        urllist.append(getImg(html))
    return urllist
print(haibao("0169547"))

