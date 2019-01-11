#coding:utf-8
import requests
import json
import re

host = 'http://user.bookan.com.cn/index.php?'
user_agent = {'headers':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

def get_id(url):
    #url = raw_input('请输入目标网址：')
    list = re.findall('\d+\.?\d*',url)
    id1 = list[1] #1512
    id2 = list[2] #447815
    return id1,id2
print get_id(raw_input("输入："))[0]

