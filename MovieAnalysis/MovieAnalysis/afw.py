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
    print(str(aa)[A+9:B+4])

haibao('0167260')