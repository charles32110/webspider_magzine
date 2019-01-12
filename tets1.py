#coding:utf-8
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



import requests
import json
import re
import threading
import Queue
import time


#定义全局数据
q_src=Queue.LifoQueue()
q_draw=Queue.LifoQueue()

class Spider(object):

    def __init__(self):
        self.url = raw_input('请输入目标网址：')
        self.url1 = 'http://user.bookan.com.cn/index.php?'
        self.user_agent = {'headers':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
        self.list = re.findall('\d+\.?\d*',self.url)
        self.id1 = self.list[1] #1512
        self.id2 = self.list[2] #447815
        params1 = {
            'op': 'Resource.issueInfoList',
            'instanceId': '1477',
            'resourceType': '1',
            'issueIds': self.id2
        }
        a = requests.get(self.url1, headers=self.user_agent, params=params1)
        data = a.json()['data']
        # resourceId = data[0]['resourceId']
        self.count = data[0]['count'] # pagenumber
        self.webpage = data[0]['jpg']  #pagetype//jpej3/5
        self.fname = data[0]['resourceName'] + data[0]['issueName']  # 文件名称
        print('————初始化完成————找到所属目录————')



    def get_hash(self):
        params2 = {
            'op': 'Resource.getHash',
            'resourceType': '1',
            'resourceId': self.id1,
            'issueId': self.id2,
            'start': '1',
            'end': self.count
        }
        b = requests.get(self.url1, headers=self.user_agent, params=params2)
        data2 = b.json()['data']
        global q_src
        for dd in data2:
            h = dd[u'hash']
            p = dd['page']
            h = 'http://img-qn.bookan.com.cn/jpage' + self.webpage + '/' + self.id1 + '/' +\
                '%s-%s' % (self.id1, self.id2) + '/' + h + '_big.jpg'
            q_src.put((h,p))

    def get_content(self):
        while q_src.empty() == False:
            tup1 = q_src.get()
            pic = requests.get(tup1[0])#图片内容
            q_draw.get(pic,tup1[1])#图片内容加名称
        else:
            print ('提取结束')
    def fast(self):
        for nu in range(1, 6):
            t1 = threading.Thread(target=self.get_content)
            t1.start()


    def get_pic(self):
        while q_draw.empty() == False:
            tup2 = q_draw.get()
            with open('pict/%s'%tup2[1],'ab') as f:#以名称数字打开图片
                f.write(tup2.get()[0])#写入内容
                f.close()
        else:
            print ('下载完成')

    def fast2(self):
        for nu in range(1, 6):
            t2= threading.Thread(target=self.get_pic())
            t2.start()

if __name__ == '__main__':
    test = Spider()
    test.get_hash()
    test.fast()

    test.get_pic()
    test.fast2()
    #li = Queue.Queue()
    #test.get_content()
    #test.get_content(test.get_hash())
    #test.formsrc(test.get_hash(test.get_par1()['page']))
    #test.get_hash(test.get_par1()['page'], test.get_par1()['pagetype'])
