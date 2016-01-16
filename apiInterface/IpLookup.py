#coding=utf-8
__author__ = 'lgx'

import requests
import json

class IpLookup(object):

    def __init__(self,ip):
        self.ip = ip

    def getIpInfo(self):
        header = {'apikey':'edca0f473f30494db08da4b090ba506a'}
        args = {'ip':self.ip}
        r = requests.get('http://apis.baidu.com/apistore/iplookupservice/iplookup',params=args,headers=header)
        return self.getFormatIpInfo(r.text)

    def getFormatIpInfo(self,data):
        json_data = json.loads(data)
        detail_data = json_data['retData']
        l = []
        for key,item in detail_data.items():
            if key == 'country':
                l.append('国家:'+item.encode('utf-8'))
            elif key == 'province':
                l.append('省份:'+item.encode('utf-8'))
            elif key == 'city':
                l.append('城市:'+item.encode('utf-8'))
            elif key == 'district':
                l.append('地区:'+item.encode('utf-8'))
            elif key == 'carrier':
                l.append('运营商:'+item.encode('utf-8'))
        return l