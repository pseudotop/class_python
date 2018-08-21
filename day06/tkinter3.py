from tkinter import *
import datetime
import time

def call_tkinter():
    window = Tk()
    label = Label(window, text="시간")
    label2 = Label(window, text="")
    label.pack(side=LEFT,padx=10)
    label2.pack(side=LEFT,padx=10)
    label2["text"] = str("일어나세요")
    window.mainloop()

def listen(callback):
    while True:
        dt = datetime.datetime.now()
        print(dt)
        if (dt > datetime.datetime(2018, 8, 14, 11, 45, 0, 0)):
            callback()
            break
        # cpu usage를 줄이기 위해 sleep 사용
        time.sleep(0.03)

listen(call_tkinter())