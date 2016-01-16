#coding=utf-8
__author__ = 'lgx'
import requests
import json

class Robot(object):

    def __init__(self, msg):
        self.msg = msg

    def chat(self):
        args = {'key':'879a6cb3afb84dbf4fc84a1df2ab7319', 'info':self.msg, 'userid':'eb2edb736'}
        header = {'apikey':'edca0f473f30494db08da4b090ba506a'}
        r = requests.get('http://apis.baidu.com/turing/turing/turing', params=args, headers=header)
        return json.loads(r.text)['text']