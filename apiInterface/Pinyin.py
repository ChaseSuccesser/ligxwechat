#coding=utf-8
__author__ = 'lgx'

import requests
import json

class Pinyin(object):

    def __init__(self, string):
        self.string = string

    def getPinyin(self):
        args = {'str':self.string}
        header = {'apikey':'edca0f473f30494db08da4b090ba506a'}
        r = requests.get('http://apis.baidu.com/xiaogg/changetopinyin/topinyin', params=args, headers=header)
        return r.text.replace(' ','')