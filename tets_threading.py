#coding:utf-8
import thread
import threading
import requests
import re

import requests
import json
import re
import threading

class Spider(object):

    def __init__(self):
        self.url = raw_input('请输入目标网址：')
        self.url1 = 'http://user.bookan.com.cn/index.php?'
        self.user_agent = {'headers':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
        self.list = re.findall('\d+\.?\d*',self.url)
        self.id1 = self.list[1] #1512
        self.id2 = self.list[2] #447815
        print('————初始化完成————')

    def get_par1(self):
        params1 = {
            'op': 'Resource.issueInfoList',
            'instanceId': '1477',
            'resourceType': '1',
            'issueIds': self.id2
        }

        a = requests.get(self.url1, headers=self.user_agent, params=params1)
        data = a.json()['data']
        #resourceId = data[0]['resourceId']
        count = data[0]['count']  #pagenumber
        webpage = data[0]['jpg']
        fname = data[0]['resourceName'] + data[0]['issueName'] #文件名称
        print('————找到所属目录————')
        return {'page':count,
                'pagetype':webpage,
                'fname':fname}


    def get_hash(self,count):
        params2 = {
            'op': 'Resource.getHash',
            'resourceType': '1',
            'resourceId': self.id1,
            'issueId': self.id2,
            'start': '1',
            'end': count
        }
        print params2
if __name__ == '__main__':
    spider = Spider()
    spider.get_hash(spider.get_par1()['page'])
