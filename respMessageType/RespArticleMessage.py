#coding=utf-8
from respMessageType.RespBaseMessage import RespBaseMessage

__author__ = 'lgx'

class RespArticleMessage(RespBaseMessage):

    '''
    ArticleCount:图文消息个数，限制为10条以内
    Articles:多条图文消息信息，默认第一个item为大图,注意，如果图文数超过10，则将会无响应
    '''
    def __init__(self,toUserName,fromUserName,createTime,msgType,funcFlag,articleCount,articleList):
        super(RespArticleMessage,self).__init__(toUserName,fromUserName,createTime,msgType,funcFlag)
        self.articleCount = articleCount
        self.articleList = articleList

    def getArticleCount(self):
        return self.articleCount

    def getArticleList(self):
        return self.articleList