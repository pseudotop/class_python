from tkinter import *
import time

window = Tk()

w = Canvas(window, width=300, height=200)
w.pack()

# w.create_rectangle(50, 25, 200, 100, fill="blue")
# w.create_line(0,0,300,200)
# w.create_line(0,0,300,100,fill="red")
id = w.create_oval(10,100,50,150,fill="green")


# for i in range(100):
#     w.move(id,1,0)
#     window.update()
#     time.sleep(0.05)
def move_right(ev):
    print(ev)
    w.move(id,5,0)

w.bind_all('<ButtonPress-3>',move_right)

window.mainloop()
