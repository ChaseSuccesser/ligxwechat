#coding=utf-8
from reqMessageType.ReqBaseMessage import ReqBaseMessage

__author__ = 'lgx'

class ReqLinkMessage(ReqBaseMessage):

    '''
    消息标题:Title;
    消息描述:Description;
    消息链接:Url;
    '''

    def __init__(self,toUserName,fromUserName,createTime,msgType,msgId,title,description,url):
        super(ReqLinkMessage,self).__init__(toUserName,fromUserName,createTime,msgType,msgId)
        self.title = title
        self.description = description
        self.url = url

    def getTitle(self):
        return self.title

    def getDescription(self):
        return self.description

    def getUrl(self):
        return self.url
