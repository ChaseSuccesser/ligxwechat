#coding=utf-8
__author__ = 'lgx'

class Article(object):

    '''
    title:图文消息名称
    description:图文消息描述
    picUrl:图片链接，支持JPG、PNG格式，较好的效果为大图640*320，小图80*80，限制图片链接的域名需要与开发者填写的基本资料中的Url一致
    url:点击图文消息跳转链接

    发送图文消息需要注意的地方:
    图文消息的标题、描述中可以使用QQ表情、符号表情，但不支持超文本链接
    图文消息的链接、图片链接可以使用外部域名下的资源
    '''

    def __init__(self,title,description,picUrl,url):
        self.title = title
        self.description = description
        self.picUrl = picUrl
        self.url = url

    def getTitle(self):
        return self.title

    def getDescription(self):
        return self.description

    def getPicUrl(self):
        return self.picUrl

    def getUrl(self):
        return self.url