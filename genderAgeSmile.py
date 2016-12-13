#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# $File: hello.py

# You need to register your App first, and enter you API key/secret.
# 您需要先注册一个App，并将得到的API key和API secret写在这里。
#API_KEY = '<your API key here>'
#API_SECRET = '<your API secret here>'
API_KEY = '8dd67f05e50669f09f6bc8dd9153f5d4'
API_SECRET = 'TLc7GR3PEeLEbO7bfftnJGgRpLRTomd3'

# First import the API class from the SDK
# 首先，导入SDK中的API类
from facepp import API

api = API(API_KEY, API_SECRET)

#define a function to get certain attribute
def getAttr(url, attrname):
	faceres = api.detection.detect(url = url)
	attrres = faceres['face'][0]['attribute'][attrname]
	return attrres;


myurl = 'http://img1.gtimg.com/ent/pics/hv1/215/252/1887/122766650.jpg'
myage = getAttr(myurl, 'age')
mygender = getAttr(myurl, 'gender')
mysmile = getAttr(myurl, 'smiling')

print 'myage: '
print myage
print 'mygender: ' 
print mygender
print 'mysmile: '
print mysmile 

