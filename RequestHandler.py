#coding=utf-8
from flask import Flask,request,make_response,url_for
import hashlib
import time
from respMessageType.RespTextMessage import RespTextMessage
from respMessageType.Article import Article
from respMessageType.RespArticleMessage import RespArticleMessage
from util import MessageUtil
from apiInterface.Weather import Weather
from apiInterface.IpLookup import IpLookup
from apiInterface.Girl import Girl
from apiInterface.Attraction import Attraction
from apiInterface.Robot import Robot

app = Flask(__name__)
app.debug = True

@app.route('/',methods=['GET'])
def wechatAuth():
    token = 'ligx'
    requestArgs = request.args
    signature = requestArgs.get('signature','')
    timestamp = requestArgs.get('timestamp','')
    nonce = requestArgs.get('nonce','')
    echostr = requestArgs.get('echostr','')

    arr = [timestamp,nonce,token]
    arr.sort()
    sortResult = ''.join(arr)
    sha1Result = hashlib.sha1(sortResult).hexdigest()

    if sha1Result == signature:
        response = make_response(echostr)
        response.content_type = 'content-type:text'
        return response
    return sha1Result

@app.route('/',methods=['POST'])
def parseMsg():
    requestData = request.data
    map = MessageUtil.parseXml(requestData)
    fromUserName = map['FromUserName']
    toUserName = map['ToUserName']
    msgType = map['MsgType']
    content = map['Content'].encode('utf-8')

    #帮助信息
    if content == 'help':

        help_info = '养眼/色 : "美女"\n'
        help_info += 'ip查询 : "xxx.xxx.xxx.xxx"\n'
        help_info += '天气查询 : "天气:北京"\n'
        help_info += '景点查询 : "景点:xxx"\n'
        help_info += '机器人聊天'

        textMessage = RespTextMessage(fromUserName,toUserName,str(int(time.time())),'text','0',help_info)
        xmldata = MessageUtil.messageToTextXml(textMessage)

    #文章查看
    elif content == '文章':
        title = '这是标题'
        description = '这是描述这是描述这是描述这是描述这是描述这是描述'
        picUrl = url_for('static',filename='1.png',_external=True)
        url = 'http://blog.csdn.net/u010567606'
        article = Article(title,description,picUrl,url)
        articleList = [article]

        articleMessage = RespArticleMessage(fromUserName,toUserName,str(int(time.time())),'news','0',str(len(articleList)),articleList)
        xmldata = MessageUtil.messageToArticleXml(articleMessage)

    #养眼美女
    elif content == '美女':
        girl = Girl()
        articleList = girl.getGirlImage()

        articleMessage = RespArticleMessage(fromUserName,toUserName,str(int(time.time())),'news','0',str(len(articleList)),articleList)
        xmldata = MessageUtil.messageToArticleXml(articleMessage)

    #ip地址查询
    elif content.count('.')==3:
        ipLookup = IpLookup(content)
        l = ipLookup.getIpInfo()
        ipInfo = ''
        for item in l:
            ipInfo += item + '\n'

        textMessage = RespTextMessage(fromUserName,toUserName,str(int(time.time())),'text','0',ipInfo)
        xmldata = MessageUtil.messageToTextXml(textMessage)

    #景点查询
    elif content[0:content.find(':')] == '景点':
        attraction = Attraction(content[content.find(':')+1:])
        l = attraction.getAttractionInfo()
        attraction_info = ''
        for item in l:
            attraction_info += item + '\n\n'
        textMessage = RespTextMessage(fromUserName,toUserName,str(int(time.time())),'text','0',attraction_info)
        xmldata = MessageUtil.messageToTextXml(textMessage)

    #天气查询
    elif content[0:content.find(':')] == '天气':
        weather = Weather(content[content.find(':')+1:])
        weatherInfoList = weather.getWeatherAllInfo()
        weatherinfo = ''
        for item in weatherInfoList:
            weatherinfo += item+'\n'

        textMessage = RespTextMessage(fromUserName,toUserName,str(int(time.time())),'text','0',weatherinfo)
        xmldata = MessageUtil.messageToTextXml(textMessage)

    else:
        robot = Robot(content)
        msg = robot.chat()

        textMessage = RespTextMessage(fromUserName,toUserName,str(int(time.time())),'text','0',msg)
        xmldata = MessageUtil.messageToTextXml(textMessage)

    response = make_response(xmldata)
    response.content_type = 'application/xml'
    return response


@app.route('/hello',methods=['GET'])
def ping():
    weather = Weather('beijing')
    weatherInfoList = weather.getWeatherAllInfo()
    weatherinfo = ''
    for item in weatherInfoList:
        weatherinfo += item+'\n'
    response = make_response(weatherinfo)
    return response