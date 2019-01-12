#coding:utf-8
import requests
from reportlab.pdfgen import canvas
import os
import time
import re
import Queue
import threading




pagecontent = Queue.Queue()
host = 'http://user.bookan.com.cn/index.php?'
user_agent = {'headers':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

class Spider(object):
    #初始化所有复用的量
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
        for dd in data2:
            h = dd[u'hash']
            p = dd['page']
            h = 'http://img-qn.bookan.com.cn/jpage' + self.webpage + '/' + self.id1 + '/' +\
                '%s-%s' % (self.id1, self.id2) + '/' + h + '_big.jpg'
            pagecontent.put((p,h))


    def get_content(self):
        pagepc = pagecontent.get()
        psrc = pagepc[1]
        ppage = pagepc[0]
        pice = requests.get(psrc,headers = user_agent)
        with open('/Users/zhangguanqin/PycharmProjects/tets/pict/%s.jpg'%ppage,'ab')as f:
            f.write(pice.content)
            f.close()
        print ('完成第%s页'%ppage)

    def convert_images_to_pdf():
        pages = 0
        (w, h) = (600, 840)
        c = canvas.Canvas('/Users/zhangguanqin/PycharmProjects/tets/%s' % time.asctime() + '.pdf')
        l = os.listdir('/Users/zhangguanqin/PycharmProjects/tets/pict')
        l.sort(key=lambda x: int(x[:-4]))
        for i in l:
            f = '/Users/zhangguanqin/PycharmProjects/tets/pict' + os.sep + str(i)
            c.drawImage(f, 0, 0, w, h)
            c.showPage()
            pages = pages + 1
        c.save()


    def fast(self):
        t1 = threading.Thread(target=self.get_hash)
        t1.start()
        t1.join()
        print ('————完成页码标定————')
        for i in range(1,5):
            while not pagecontent.empty():
                t2 = threading.Thread(target=self.get_content)
                t2.start()




if __name__ == '__main__':
    spider= Spider()
    spider.fast()
    #spider.get_pic()








'''     

        pagelist = pagelist[1:]
'''
