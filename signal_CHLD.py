#coding:utf8
'''
    子进程结束后会向父进程发送SIGCHLD信号
'''

import os
import signal
from time import sleep

def onsigchld(a,b):
    print '收到子进程结束号'

signal.signal(signal.SIGCHLD,onsigchld)#signal 处理的函数必须需要两个参数

pid = os.fork()
if pid == 0:
    print '我是子进程，pid是',os.getpid()
    print 'gggggggggggggggggggg'
    sleep(4)
else:
    print '我是父进程，pid是',os.getpid()
    os.wait() #等待子进程结束
