#coding:utf8

import os
import signal
from time import sleep
import Queue

QCOUNT = Queue.Queue()#初始化队列

def onsigchld(a,b):
    '''收到信号后向队列中插入一个数字1'''
    print '收到SIGUSR1信号'
    sleep(2)
    QCOUNT.put(1)#向队列中写入1


def exithanddle(s,e):
    raise SystemExit('收到终止命令，退出程序')


signal.signal(signal.SIGUSR1,onsigchld)#绑定信号处理函数
signal.signal(signal.SIGINT,exithanddle)#当按下CTRL+c
#SIGUSR1 - 2 用户自定义信号
while 1:
    print '我的pid是',os.getpid()
    print '现在队列元素的个数是',QCOUNT.qsize()
    sleep(5)

