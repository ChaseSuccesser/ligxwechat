#coding=utf-8
from respMessageType.RespBaseMessage import RespBaseMessage

__author__ = 'lgx'

class RespTextMessage(RespBaseMessage):

    '''
    content:回复的消息内容

    在微信公众帐号的文本消息中，换行符仍然是“\n”
    文本消息中使用网页超链接:正确的用法是将a标签href属性的值用双引号引起,eq:<a href="http://blog.csdn.net/lyq8479">点我</a>
    '''

    def __init__(self,toUserName,fromUserName,createTime,msgType,funcFlag,content):
        super(RespTextMessage,self).__init__(toUserName,fromUserName,createTime,msgType,funcFlag)
        self.content = content

    def getContent(self):
        return self.content