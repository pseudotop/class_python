from tkinter import *

window = Tk()

b1 = Button(window, text="Hello World!1")
b2 = Button(window, text="Hello World!2")
b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b1["text"] = "ONE"
b2["text"] = "TWO"

window.mainloop()