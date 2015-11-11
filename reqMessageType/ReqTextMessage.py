#coding=utf-8
from reqMessageType.ReqBaseMessage import ReqBaseMessage

__author__ = 'lgx'

class ReqTextMessage(ReqBaseMessage):
    def __init__(self,toUserName,fromUserName,createTime,msgType,msgId,content):
        super(ReqTextMessage,self).__init__(toUserName,fromUserName,createTime,msgType,msgId)
        self.content = content

    def getContent(self):
        return self.content