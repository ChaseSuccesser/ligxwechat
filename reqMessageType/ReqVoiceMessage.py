#coding=utf-8
from reqMessageType.ReqBaseMessage import ReqBaseMessage

__author__ = 'lgx'

class ReqVoiceMessage(ReqBaseMessage):

    '''
    媒体ID:MediaId;
    语音格式:Format;
    '''

    def __init__(self,toUserName,fromUserName,createTime,msgType,msgId,mediaId,format):
        super(ReqVoiceMessage,self).__init__(toUserName,fromUserName,createTime,msgType,msgId)
        self.mediaId = mediaId
        self.format = format

    def getMediaId(self):
        return self.mediaId

    def getFormat(self):
        return self.format