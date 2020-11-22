import json
import os
import socket
import sys
import threading
import time
import tkinter as tk
from tkinter import *


def get_drug(Text):
    file = open("drug.txt", encoding="utf-8")
    str_i = file.read()
    global drug
    drug = json.loads(str_i)
    print(drug)
    file.close()
    file2 = open("drugInfo.txt", encoding="utf-8")
    str_i = file2.read()
    global drugInfo
    drugInfo = json.loads(str_i)
    print(drugInfo)
    file2.close()
    Text.delete('1.0', 'end')
    for i in drug:
        name = ""
        for j in drugInfo:
            if i.get("drugid") == j.get("drugid"):
                name = j.get("name")
        Text.insert(INSERT, "药槽：" + str(i.get("slotid")) + " 名称: " + name + " 剩余量: " + str(i.get("remain")) + "\n")


root = tk.Tk()
root.geometry("800x480")
root.resizable(0, 0)
root.title("东大智能药箱GUI")
drug = {}
drugInfo = {}

v = tk.StringVar()
L1 = tk.Label(root, text="东大智能药箱系统", font=("宋体", 30, "bold"))
L1.place(x=220, y=20)
L2 = tk.Label(root, text='网络状态：', font=("宋体", 10, "bold"))
L3 = tk.Label(root, text='等待连接', font=("宋体", 10, "bold"), textvariable=v)  # , textvariable=v
L2.place(x=20, y=70)
L3.place(x=85, y=70)
B1 = tk.Button(root, text="退出", font=("宋体", 10, "bold"), command=lambda: os._exit(1))
B1.place(x=10, y=10)
B2 = tk.Button(root, text="放入新药物", font=("宋体", 20, "bold"))
B2.place(x=20, y=100)
# B3 = tk.Button(root, text="获取信息", font=("宋体", 20, "bold"), command=lambda: get_drugInfo())
# B3.place(x=20, y=150)
T1 = Text(root, width=50, height=12)
T1.place(x=20, y=200)
get_drug(T1)


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
                sys.stdout.write("\r连接成功")
                sys.stdout.flush()
                v.set("连接成功")
                status = 1
                time.sleep(1)
                while True:
                    s.send(a)
                    time.sleep(3)
            except socket.error:
                sys.stdout.write("\rsocket 错误，重连ing....")
                sys.stdout.flush()
                v.set("断线重连....")
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


def thread_it(func, *args):
    """将函数打包进线程"""
    # 创建
    t = threading.Thread(target=func, args=args)  # 守护 !!!
    t.setDaemon(True)  # 启动
    t.start()  # 阻塞--卡死界面！


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
root.mainloop()
thread1.join()
thread2.join()
print("退出主线程")
