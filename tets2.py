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
print resourceId
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
pageid = []
#print (data2['hash'])
for x in data2:
    pageid.append(x['hash'])
#(w, h) = portrait(A4)
n = 1
for m in pageid:
    src = 'http://img-qn.bookan.com.cn/jpage5/' + '1512' + '/' + '1512-447815' +'/'+ m +'_big.jpg'
    p = requests.get(url= src, headers= headers)
    #c = canvas.Canvas('/PycharmProject/tets/%s.pdf' % fname, pagesize=portrait(A4))
    #c.drawImage(p, 0, 0, w, h)
    with open('pict/%s.jpg'%n,'ab') as f:
        f.write(p.content)
        f.close()
        print('完成%s'%n)
        n = n+1






