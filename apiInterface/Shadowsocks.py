#coding=utf-8
__author__ = 'lgx'

#coding=utf-8

'''
import bs4
import requests

def getFreeAccount():
    url = 'http://www.ishadowsocks.com'
    r = requests.get(url)
    data = r.content.decode()

    content = bs4.BeautifulSoup(data,from_encoding='utf-8')
    divList = content.findAll('div',attrs={'class':'col-lg-4 text-center'})

    freeAccount = []
    for index,divItem in enumerate(divList):
        if index == 3:
            break
        i = 0
        for index2,child in enumerate(divItem.children):
            if i==8:
                break
            freeAccount.append(str(child.string))
            i += 1
    return freeAccount
'''