#coding=utf-8
from reqMessageType.ReqBaseMessage import ReqBaseMessage

__author__ = 'lgx'

class ReqImageMessage(ReqBaseMessage):

    '''
    picUrl:图片链接
    '''

    def __init__(self,toUserName,fromUserName,createTime,msgType,msgId,picUrl):
        super(ReqImageMessage,self).__init__(toUserName,fromUserName,createTime,msgType,msgId)
        self.picUrl = picUrl

    def getPicUrl(self):
        return self.picUrl