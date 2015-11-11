#coding=utf-8
__author__ = 'lgx'

import os
import sys
root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, 'site-packages'))


import sae
from RequestHandler import app

application = sae.create_wsgi_app(app)