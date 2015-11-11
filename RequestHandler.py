#coding=utf-8
from flask import Flask,request,make_response,url_for
import hashlib
import time
from respMessageType.RespTextMessage import RespTextMessage
from respMessageType.Article import Article
from respMessageType.RespArticleMessage import RespArticleMessage
from util import MessageUtil
from apiInterface.Weather import Weather

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
    content = map['Content']

    if content.encode('utf-8') == '文章':
        title = '这是标题'
        description = '这是描述这是描述这是描述这是描述这是描述这是描述'
        picUrl = url_for('static',filename='1.png',_external=True)
        url = 'http://blog.csdn.net/u010567606'
        article = Article(title,description,picUrl,url)

        articleList = [article]
        articleMessage = RespArticleMessage(fromUserName,toUserName,str(int(time.time())),'news','0',str(len(articleList)),articleList)
        xmldata = MessageUtil.messageToArticleXml(articleMessage)
    else:
        weather = Weather(content)
        weatherInfoList = weather.getWeatherAllInfo()
        weatherinfo = ''
        for item in weatherInfoList:
            weatherinfo += item+'\n'
        textMessage = RespTextMessage(fromUserName,toUserName,str(int(time.time())),'text','0',weatherinfo)
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