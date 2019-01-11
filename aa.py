#coding:utf-8
import urllib2
import re
import os
class Spider(object):
#声明爬虫
    def __init__(self):
        self.url = 'http://www.maiziedu.com/course/teachers/?page=%s'
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
    # 获取网页代码
    def get_page(self, page_index):
        headers ={'User-Agent': self.user_agent}
        try:
            request = urllib2.Request(url = self.url%str(page_index), headers = headers)
            response = urllib2.urlopen(request)
            content = response.read()
            return content
        except urllib2.HTTPError as e :
            print '无法访问'
            exit()
    def analysis(self, content):
        pattern = re.compile('<a href="/p/-?[1-9]\d*" title="(.*?)</a></div><div class="threadlist_author pull_right">', re.S)
        items = re.findall(pattern, content)
        return items
     # 保存内容
    def save(self, items, path):
        for item in items:
            path = 'maizi2'
            if not os.path.exists(path):
                os.makedirs(path)
                    # 还有mkdir（path）
            file_path = path + '/' + item[0] + '.txt'
            f = open(file_path, 'w')
            f.write(item[1])
            f.close()
    def run(self):
        print('开始抓啦')
        for i in range(1, 35):
            content = self.get_page(i)
            items = self.analysis(content)
            self.save(items, 'maizi')
        print('抓取完毕')
if __name__ == '__main__':
    spider = Spider()


