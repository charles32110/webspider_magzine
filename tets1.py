'''
import requests
url = 'http://user.bookan.com.cn/index.php?'
headers = {
"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
params1 = {
    'op': 'Resource.issueInfoList',
    'instanceId': '3334',
    'resourceType': '1',
    'issueIds': '448859'
}

a = requests.get(url, headers = headers, params=params1)
print a.json()

class mm(object):
    def __init__(self):
        self.x = 5
        self.y = 6
    def cal1(self):
        m = self.x + self.y
        return m
    def cal2(self,m):
        q = m*m
        print q
if __name__ == '__main__':
    a = mm()

    a.cal2(a.cal1())

#coding:utf-8
import requests
import json
import os
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait, landscape
url = 'http://user.bookan.com.cn/index.php?'
headers = {
"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
params1 = {
    'op': 'Resource.issueInfoList',
    'instanceId': '1477',
    'resourceType': '1',
    'issueIds': '447815'
}

a = requests.get(url, headers = headers, params=params1)
data = a.json()['data']
resourceId = data[0]['resourceId']
count = data[0]['count']
fname = data[0]['resourceName'] + data[0]['issueName']

params2 = {
    'op':'Resource.getHash',
    'resourceType': '1',
    'resourceId': resourceId,
    'issueId': '447815',
    'start': '1',
    'end': count
}
b = requests.get(url, headers = headers, params=params2)
data2 = b.json()['data']
print b.json()


import requests
def get_hash():
    user_agent = {
        'headers': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    url1 = 'http://user.bookan.com.cn/index.php?'
    params2 = {
        'op': 'Resource.getHash',
        'resourceType': '1',
        'resourceId': 1512,
        'issueId': 447815,
        'start': '1',
        'end': 124
    }
    b = requests.get(url1, headers=user_agent, params=params2)
    data2 = b.json()['data']
    print b.json()
get_hash()

a = "saaskld"
b = "askj"
print ('%s-%s'%(a,b))

import threading

def x():
    a = 3
    b = 4
    c = 5
    return a, b, c
print (x()[1])
'''
import thread