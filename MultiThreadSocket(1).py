import socket
import threading
import time
import uuid


def doConnect(host, port):
    sock = socket.socket()
    try:
        sock.connect((host, port))
    except:
        pass
    return sock


class myThread1(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            try:
                a = "HeartBeat"
                a = a.encode()
                # mac = hex(uuid.getnode())[2:]
                # mac = '-'.join(mac[i:i + 2] for i in range(0, len(mac), 2))
                mac = '11-11-11-11-11-11'
                global s, status
                s.send(mac.encode())
                print("连接成功")
                status = 1
                time.sleep(1)
                while True:
                    s.send(a)
                    time.sleep(3)
            except socket.error:
                print("socket 错误，重连ing....")
                status = 0
                s = doConnect(host, port)
                time.sleep(1)


class myThread2(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global status
        while status == 1:
            str = s.recv(1024).decode()
            print(str)


host = "127.0.0.1"
port = 8086
s = doConnect(host, port)
status = 0

# 创建新线程
thread1 = myThread1()
thread2 = myThread2()

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("退出主线程")
