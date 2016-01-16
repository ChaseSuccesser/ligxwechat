#coding=utf-8
__author__ = 'lgx'
from respMessageType.Article import Article
import requests
import json

class Girl(object):

    def __init__(self):
        self.num = 2

    def getGirlImage(self):
        header = {'apikey':'edca0f473f30494db08da4b090ba506a'}
        args = {'num':self.num}
        r = requests.get('http://apis.baidu.com/txapi/mvtp/meinv', params=args, headers=header)
        return self.getFormatGirlImage(r.text)

    def getFormatGirlImage(self,data):
        girl_image_jsondata = json.loads(data)
        articleList = []
        for index in range(0,self.num-1):
            girl_image_detailinfo = girl_image_jsondata[str(index)]
            title = girl_image_detailinfo['title']
            description = girl_image_detailinfo['description']
            picurl = girl_image_detailinfo['picUrl']
            url = girl_image_detailinfo['url']
            article = Article(title,description,picurl,url)
            articleList.append(article)
        return articleList