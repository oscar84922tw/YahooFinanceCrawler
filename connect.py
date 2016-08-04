# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import lxml
import urllib
import csv
from itertools import izip

class Connecter:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        }

    def getContent(self, url, headers):
        res = requests.get(url,headers)
        res.encoding = 'utf-8'
        return BeautifulSoup(res.text, 'lxml')


    def getFirstPage(self,url):
        print("getFirstPage")
        content = self.getContent("https://tw.money.yahoo.com/fund/domestic", self.headers)
        links = []
        
        # for Coin in content.find
        for link in content.find_all('a'):
            if "/fund/cpflist/FUND_DOMESTIC_PROVIDER:" in str(link.get('href')):
                links.append("https://tw.money.yahoo.com/" + str(link.get('href')))
        # print(links)
        return links

    def getFileTag(self,url):
        content = self.getContent(url,self.headers)
        # print("!!!!!!!!!!!!!!!!!!!!!!content: " + str(content))
        links = []
        profileData = []
        currencies = []
        currency = content.findAll(lambda tag: tag.name == 'td' and tag.get('class') == ['Ell','Ta-c'])
        # currency = content.findAll("td", { "class" : ["Ell","Ta-c"]})
        
        # print(type(currency))
        # for txt in currency:
        #     cc = txt.string.strip()
        #     currencies.append(cc)
        #     print cc
        # print currency
        
        for link,txt in izip(content.find_all('a'),currency):
            print link
            if "/fund/summary/" in str(link.get('href')):
                print "yeeeeeeeeee"
                # links.append("https://tw.money.yahoo.com" + str(link.get('href').replace("summary","history")))
                links.append(str(link.get('href')[14:]))
                print(type(link))
                fileName = str(link.get('href')[14:24])
                cc = txt.string.strip()
                profileData.append([fileName,link.string.encode('utf8'),cc.encode('utf8')])
                # print(profileData)
                
        # print(links)
        
        f = open("profile.csv","w")
        w = csv.writer(f)
        w.writerows(profileData)
        f.close()
        
        return links


