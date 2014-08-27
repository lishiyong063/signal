#coding:utf8

'''
使用多线程向另一个进程发送信号
'''
import threading
import os
import signal

def sendusr1():
    print '发送信号'
    #这里的进程id需要写接收程序产生的pid
    os.kill(5619,signal.SIGUSR1)

WORKER = []

for i in range (1,7):
    threadstance = threading.Thread(target = sendusr1)
    WORKER.append(threadstance)

for i in WORKER:
    i.start()

for i in WORKER:
    i.join()

print '主线程完成'
