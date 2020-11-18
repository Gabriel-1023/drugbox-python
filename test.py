from tkinter import *

root = Tk()
text = Text(root,width=20,height=15)
text.pack()
text.insert(INSERT,"I love Python3") #INSERT索引表示插入光标当前的位置
def show():
    print("被点了一下。。。")
b1 = Button(text,text="点我",command=show)
text.window_create(INSERT,window=b1)
mainloop()
