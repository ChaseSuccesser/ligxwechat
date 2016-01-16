#coding=utf-8
__author__ = 'lgx'

import redis
import time
import datetime
import os

class RedisUtil(object):

    def __init__(self,db):
        self.db = db

    def getRedisConnection(self):
        "Connection of Redis"
        redisConn = redis.Redis(host='123.57.66.199', port='6379', db=self.db, password='eyuankuwant')
        return redisConn

    def getKey(self, mode, key):
        redisConn = self.getRedisConnection()

        if mode == 'string':
            value = redisConn.get(key)

        return value

    def getAllKeys(self):
        "获取所有的key"
        redisConn = self.getRedisConnection()

        allKeys = redisConn.keys('*')
        key_detail_info_list = []
        format = '%Y-%m-%d %H:%M:%S'
        for key in allKeys:
            key_expire_time = datetime.datetime.fromtimestamp(int(time.time())+redisConn.ttl(key)).strftime(format) if redisConn.ttl(key) is not None else ''
            key_type = redisConn.type(key).decode('utf-8')
            key_detail_info_list.append(key.decode('utf-8')+'   '+key_type+'   超时时间:'+key_expire_time)

        return key_detail_info_list

    def delKey(self, mode, key):
        redisConn = self.getRedisConnection()
        if mode == 'string':
            result = redisConn.delete(key)
        return result


if __name__ == '__main__':
    redisUtil = RedisUtil(0)

    result = redisUtil.delKey('string','design_template_theme')
    print(result)

    '''
    materialKindCacheValue = redisUtil.getKey('string', 'all_material_kind')

    print('oneLevelKind_id--->'.encode('utf-8')+ materialKindCacheValue if materialKindCacheValue is not None else '')

    with open('D:\cache2.txt', mode='w') as f:
        f.write(str(materialKindCacheValue))

    print('查询缓存完成')


    key_detail_info_list = redisUtil.getAllKeys()

    os.remove('D:\moni_redis_data.txt')
    with open('D:\moni_redis_data.txt', mode='a') as f:
        for item in key_detail_info_list:
            f.write(item+'\n')
    print('查询完成')
    '''


