import json
from datetime import datetime
import threading
import time
import pyttsx3

# i = {"215900":["阿莫西林","吃一瓶"],"215930":["复方甘草片","吃半瓶"]}
drug = {}

# i =


class myThread1(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global drug
        while True:
            time.sleep(0.5)
            now = datetime.now().strftime("%H%M%S")
            print(now)
            print(i)
            if str(now) in i:
                voice = pyttsx3.init()
                voice.say("该吃药啦！该吃药啦！"+i.get(str(now))[0]+" "+i.get(str(now))[1])
                voice.runAndWait()
                print("该吃药了"+str(i))


thread1 = myThread1()
thread1.start()

while True:
    time.sleep(5)
    file = open("test.txt",encoding="utf-8")
    str_i = file.read()
    drug = json.loads(str_i)
    file.close()
