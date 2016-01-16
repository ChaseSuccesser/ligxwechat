#coding=utf-8
__author__ = 'lgx'

import requests
import json
import sys

class Translate(object):

    def __init__(self,language,data):
        self.language = language
        self.data = data

    def translate(self):
        header = {'apikey':'edca0f473f30494db08da4b090ba506a'}

        if self.language == 'en':
            args = {'query':self.data, 'from':'en', 'to':'zh'}
        elif self.language == 'zh':
            args = {'query':self.data, 'from':'zh', 'to':'en'}

        r = requests.get('http://apis.baidu.com/apistore/tranlateservice/translate', params=args, headers=header)
        json_data_map = json.loads(r.text)
        if json_data_map['errMsg'] == 'success':
            print(json_data_map['retData']['trans_result'][0]['dst'])
        else:
            print('Don`t find translate result')

if __name__ == '__main__':
    language = sys.argv[1]
    data = sys.argv[2]
    t = Translate(language,data)
    t.translate()

