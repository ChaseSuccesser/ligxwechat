#coding=utf-8
__author__ = 'lgx'

class ReqBaseMessage(object):

    '''
    开发者微信号:ToUserName;
    发送方帐号（一个OpenID）:FromUserName;
    消息创建时间 （整型）: CreateTime;
    消息类型（text/image/location/link）:MsgType;
    消息id，64位整型: MsgId;
    '''

    def __init__(self,toUserName,fromUserName,createTime,msgType,msgId):
        self.toUserName = toUserName
        self.fromUserName = fromUserName
        self.createTime = createTime
        self.msgType = msgType
        self.msgId = msgId

    def getToUserName(self):
        return self.toUserName

    def getFromUserName(self):
        return self.fromUserName

    def getCreateTime(self):
        return self.createTime

    def getMsgType(self):
        return self.msgType

    def getMsgId(self):
        return self.msgId