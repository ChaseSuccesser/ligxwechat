#coding=utf-8
__author__ = 'lgx'

class RespBaseMessage(object):

    '''
    接收方帐号（收到的OpenID）:ToUserName;
    开发者微信号:FromUserName;
    消息创建时间 （整型）:CreateTime;
    消息类型（text/music/news）:MsgType;
    位0x0001被标志时，星标刚收到的消息:FuncFlag;
    '''

    def __init__(self,toUserName,fromUserName,createTime,msgType,funcFlag):
        self.toUserName = toUserName
        self.fromUserName = fromUserName
        self.createTime = createTime
        self.msgType = msgType
        self.funcFlag = funcFlag

    def getToUserName(self):
        return self.toUserName

    def getFromUserName(self):
        return self.fromUserName

    def getCreateTime(self):
        return self.createTime

    def getMsgType(self):
        return self.msgType

    def getFuncFlag(self):
        return self.funcFlag