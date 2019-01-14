#coding:utf-8
import requests
import time
import re
import Queue
import threading
import os
#http://user.bookan.com.cn/index.php?op=Resource.pastYearList&resourceType=1&resourceId=639
#http://user.bookan.com.cn/index.php?op=
# Resource.yearList&resourceType=1&resourceId=639&year=2018&month=0&pageNum=1&limitNum=20
yearlist = Queue.Queue()
lastlist = Queue.Queue()


class g_list(object):


    def __init__(self):
        open("目录.txt", "a")
        self.url1 = 'http://user.bookan.com.cn/index.php?'
        url2 = raw_input("输入目标网址：")
        self.user_agent = {
            'headers': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6)\
             AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
        self.list = re.findall('\d+\.?\d*', url2)
        self.id1 = self.list[1]  # 1512



    def getlist(self):
        params1 = {
            'op': 'Resource.pastYearList',
            'resourceType':'1',
            'resourceId': self.id1
        }
        a = requests.get(url=self.url1,headers = self.user_agent, params=params1)
        chart = a.json()['data']
        global yearlist
        for x in chart:
            yearlist.put((x['count'],x['year']))

    def get_url(self,year,page):
        params2 = {
            'op': 'Resource.yearList',
            'resourceType': '1',
            'resourceId': self.id1,
            'year': year,
            'month': '0',
            'pageNum': '1',
            'limitNum': page
        }
        items = requests.get(url=self.url1,headers =self.user_agent, params=params2)
        content = items.json()['data']
        global lastlist
        for ll in content:
            issueId = ll['issueId']
            issuname = ll['issueName']
            resourceName=ll["resourceName"]
            lastlist.put((issueId,issuname,resourceName))



    def book(self):
        q = lastlist.get()
        issueId = q[0]
        issuname = str(q[1]).encode('utf-8')
        resource = str(q[2]).encode('utf-8')
        finaltext = 'http://h5.magook.com/#/imgr/magazine/%s/%s/0' % (self.id1, issueId)
        with open("目录.txt", "a+") as f:  # 以追加的方式
            f.write(resource+ issuname + finaltext + '\n')
            f.close()


    def sped(self):
        t1 = threading.Thread(target=self.getlist)
        t1.start()
        t1.join()
        print ('————找到年份————')
        while not yearlist.empty():
            part = yearlist.get()
            page = str(part[0])
            year = str(part[1])
            t2 = threading.Thread(target=self.get_url,args=[year,page])
            t2.start()
            t2.join()
            print ('————取得列表正在写入————')
        while not lastlist.empty():
            t3 = threading.Thread(target=self.book)
            t3.start()







if __name__=='__main__':
    listspider = g_list()
    listspider.sped()


