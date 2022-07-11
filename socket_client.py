# -*- coding: UTF-8 -*-
import socket
import time

HOST = '127.0.0.1' # 127.0.0.1 发送数据到本地
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ts stores the time in seconds
ts = time.time() * 1.0
data = 'timestamp: %f' % (ts * 1000.0) # 希望发送的字符串
b_data = data.encode("utf-8") # 编码
s.sendto(b_data, (HOST, PORT)) # 发送数据

now = time.time()
data, sender = s.recvfrom(1024) # 等待服务区的返回数据
print("Received: " , data, "current: ", now * 1000, "From: ", sender) # 显示数据的发送方信息

data = 'quit' # 发送quit，让服务区退出
b_data = data.encode("utf-8")
s.sendto(b_data, (HOST,PORT))

s.close() # 关闭socket，节省资源