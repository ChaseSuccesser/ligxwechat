#coding=utf-8
__author__ = 'lgx'

import xml.etree.ElementTree as ET
from xml.dom import minidom

#解析用户请求的xml数据
def parseXml(xmlstr):
    root = ET.fromstring(xmlstr)

    xmlMap = {}
    for child in root:
        xmlMap[child.tag] = child.text

    return xmlMap

#响应文本数据
def messageToTextXml(messageObj):
    xml = """<xml><ToUserName><![CDATA[%s]]></ToUserName>
                 <FromUserName><![CDATA[%s]]></FromUserName>
                 <CreateTime>%s</CreateTime>
                 <MsgType><![CDATA[%s]]></MsgType>
                 <Content><![CDATA[%s]]></Content>
                 <FuncFlag>%s</FuncFlag>
               </xml>"""
    replyxml = xml % (messageObj.getToUserName(),messageObj.getFromUserName(),messageObj.getCreateTime(),
                      messageObj.getMsgType(),messageObj.getContent(),messageObj.getFuncFlag())
    return replyxml


#响应图文信息
def messageToArticleXml(messageObj):
    impl = minidom.getDOMImplementation()
    dom = impl.createDocument(None,'xml',None)
    root = dom.documentElement

    toUserNameTag = dom.createElement('ToUserName')  #创建元素节点
    toUserNameText = dom.createCDATASection(str(messageObj.getToUserName())) #创建CDATA标记
    toUserNameTag.appendChild(toUserNameText)

    fromUserNameTag = dom.createElement('FromUserName')
    fromUserNameText = dom.createCDATASection(str(messageObj.getFromUserName()))
    fromUserNameTag.appendChild(fromUserNameText)

    createTimeTag = dom.createElement('CreateTime')
    createTimeText = dom.createTextNode(messageObj.getCreateTime()) #创建文本节点
    createTimeTag.appendChild(createTimeText)

    msgTypeTag = dom.createElement('MsgType')
    msgTypeText = dom.createCDATASection(messageObj.getMsgType())
    msgTypeTag.appendChild(msgTypeText)

    articleCountTag = dom.createElement('ArticleCount')
    articleCountText = dom.createTextNode(messageObj.getArticleCount())
    articleCountTag.appendChild(articleCountText)

    articlesTag = dom.createElement('Articles')
    articles = messageObj.getArticleList()
    for index,article in enumerate(articles):
        itemTag = dom.createElement('item')

        titleTag = dom.createElement('Title')
        titleText = dom.createCDATASection(article.getTitle())
        titleTag.appendChild(titleText)

        descriptionTag = dom.createElement('Description')
        descriptionText = dom.createCDATASection(article.getDescription())
        descriptionTag.appendChild(descriptionText)

        picurlTag = dom.createElement('PicUrl')
        picurlText = dom.createCDATASection(article.getPicUrl())
        picurlTag.appendChild(picurlText)

        urlTag = dom.createElement('Url')
        urlText = dom.createCDATASection(article.getUrl())
        urlTag.appendChild(urlText)

        itemTag.appendChild(titleTag)
        itemTag.appendChild(descriptionTag)
        itemTag.appendChild(picurlTag)
        itemTag.appendChild(urlTag)

        articlesTag.appendChild(itemTag)

    root.appendChild(toUserNameTag)
    root.appendChild(fromUserNameTag)
    root.appendChild(createTimeTag)
    root.appendChild(msgTypeTag)
    root.appendChild(articleCountTag)
    root.appendChild(articlesTag)

    return root.toxml()


