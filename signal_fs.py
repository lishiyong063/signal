#coding:utf8
import os

import signal

#发送信号，16175是前面那个绑定信号处理函数的pid需要自己修改

os.kill(5512,signal.SIGTERM)

#发送信号，16175 是前面那个绑定信号处理函数的pid

os.kill(5512,signal.SIGUSR1)
