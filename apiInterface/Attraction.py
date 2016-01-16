#coding=utf-8
from Pinyin import Pinyin

__author__ = 'lgx'

import requests
import json
import sys

class Attraction(object):

    def __init__(self,attraction):
        pinyin = Pinyin(attraction)
        self.attraction = pinyin.getPinyin()

    def getAttractionInfo(self):
        args = {'id':self.attraction,'output':'json'}
        header = {'apikey':'edca0f473f30494db08da4b090ba506a'}
        r = requests.get('http://apis.baidu.com/apistore/attractions/spot', params=args, headers=header)
        return self.getFormatAttractionInfo(r.text)

    def getFormatAttractionInfo(self, data):
        json_data = json.loads(data)
        if json_data['status'] == 'Success':
            attraction_json_data = json_data['result']
            l = []
            l.append('景点名称:'+attraction_json_data['name'].encode('utf-8'))
            l.append('景点咨询电话:'+attraction_json_data['telephone'].encode('utf-8'))
            l.append('星级:'+attraction_json_data['star'].encode('utf-8'))
            l.append('价格:'+attraction_json_data['ticket_info']['price'].encode('utf-8'))
            l.append('景点开放时间:'+attraction_json_data['ticket_info']['open_time'].encode('utf-8'))
            l.append('更多事项:'+attraction_json_data['ticket_info']['attention'][0]['description'].encode('utf-8'))
            return l
        else:
            return ''
