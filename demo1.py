#coding=utf-8
import Queue
import threading
import time
q = Queue.Queue()
'''
for i in range(1,5):
    for x in range(1,5):
        q.put((i,x))

q.put(1)
q.put(2)
q.put(3)
while q.empty()==0:
    print q.get()
    time.sleep(2)
else:
    print ('wancehng')

if q.empty()==1:
    print ('asjdbc')
else:
    print ('ppppp')
'''
print time.asctime()




