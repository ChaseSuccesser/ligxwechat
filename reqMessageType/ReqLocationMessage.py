#coding=utf-8
from reqMessageType.ReqBaseMessage import ReqBaseMessage

__author__ = 'lgx'

class ReqLocationMessage(ReqBaseMessage):

    '''
    地理位置维度:Location_X;
    地理位置经度:Location_Y;
    地图缩放大小:Scale;
    地理位置信息:Label;
    '''

    def __init__(self,toUserName,fromUserName,createTime,msgType,msgId,location_x,location_y,scale,label):
        super(ReqLocationMessage,self).__init__(toUserName,fromUserName,createTime,msgType,msgId)
        self.location_x = location_x
        self.location_y = location_y
        self.scale = scale
        self.label = label

    def getLocation_X(self):
        return self.location_x

    def getLocation_Y(self):
        return self.location_y

    def getScale(self):
        return self.scale

    def getLabel(self):
        return self.label