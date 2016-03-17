#coding=utf-8
from functools import wraps
import pymysql

__author__ = 'lgx'

class Configuation(object):
    def __init__(self,env):
        if env == 'localhost':
            self.host = '127.0.0.1'
            self.port = 3306
            self.user = 'root'
            self.password = 'root'
            self.db = 'flask_app'
            self.charset = 'utf8'
        elif env == 'prod':
            self.host = ''
            self.port = ''
            self.user = ''
            self.password = ''
            self.db = ''
            self.charset = ''


def mysql(sql):
    conf = Configuation('localhost')
    def decorator(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            conn = pymysql.connect(host=conf.host, port=conf.port, user=conf.user, password=conf.password, \
                                   db=conf.db, charset=conf.charset)
            cur = conn.cursor()

            result = cur.execute(sql)
            if cur.fetchall():
                cur.scroll(0,mode='absolute')
                result = cur.fetchall()

            conn.commit()      #not required when query
            cur.close()
            conn.close()

            f(result)
        return wrap

    return decorator


@mysql('select * from user')
def query(data):
    for row in data:
        print(row)

@mysql("insert into user(name,age) values('李',24)")
def insert(data):
    if data>0:
        print('insert success!')

query()