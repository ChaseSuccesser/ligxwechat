#coding=utf-8
__author__ = 'lgx'

import requests
import json

class Weather(object):
    def __init__(self,city):
        self.city = city

    def getWeatherAllInfo(self):
        city = {'city':self.city}
        header = {'apikey':'edca0f473f30494db08da4b090ba506a'}
        r = requests.get('http://apis.baidu.com/heweather/weather/free',params=city,headers=header)
        return self.getWeatherUsefulInfo(r.text)

    def getWeatherUsefulInfo(self,data):
        s = json.loads(data)
        weatherUsefulInfpList = []
        for key in s.keys():
            weatherAllInfoMap = s[key][0]
            #-------------基本信息---------------
            basicInfoMap = weatherAllInfoMap['basic']
            weatherUsefulInfpList.append('城市纬度:'+basicInfoMap['lat'].encode("utf-8"))
            weatherUsefulInfpList.append('城市经度:'+basicInfoMap['lon'].encode("utf-8"))
            updateInfoMap = basicInfoMap['update']
            weatherUsefulInfpList.append('当地时间:'+updateInfoMap['loc'].encode("utf-8"))

            #------------实况天气----------------
            todayWeatherInfpMap = weatherAllInfoMap['now']
            weatherUsefulInfpList.append('体感温度:'+todayWeatherInfpMap['fl'].encode("utf-8"))
            weatherUsefulInfpList.append('相对湿:'+todayWeatherInfpMap['hum'].encode("utf-8"))
            weatherUsefulInfpList.append('温度:'+todayWeatherInfpMap['tmp'].encode("utf-8"))
            weatherUsefulInfpList.append('降水量:'+todayWeatherInfpMap['pcpn'].encode("utf-8"))
            weatherUsefulInfpList.append('气压:'+todayWeatherInfpMap['pres'].encode("utf-8"))
            weatherUsefulInfpList.append('能见度(km):'+todayWeatherInfpMap['vis'].encode("utf-8"))
            todayWindInfoMap = todayWeatherInfpMap['wind']
            weatherUsefulInfpList.append('风向:'+todayWindInfoMap['dir'].encode("utf-8"))
            weatherUsefulInfpList.append('风力:'+todayWindInfoMap['sc'].encode("utf-8"))
            weatherUsefulInfpList.append('风速:'+todayWindInfoMap['spd'].encode("utf-8"))
            todayStatusMap = todayWeatherInfpMap['cond']
            weatherUsefulInfpList.append('天气状况:'+todayStatusMap['txt'].encode("utf-8"))

            #------------空气质量----------------
            '''
            airInfoMap = weatherAllInfoMap['aqi']['city']
            weatherUsefulInfpList.append('空气质量指数:'+airInfoMap['aqi'].encode("utf-8"))
            weatherUsefulInfpList.append('PM2.5:'+airInfoMap['pm25'].encode("utf-8"))
            weatherUsefulInfpList.append('空气质量类别:'+airInfoMap['qlty'].encode("utf-8"))
            '''
        return weatherUsefulInfpList
