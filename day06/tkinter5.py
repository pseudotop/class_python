from tkinter import *

window = Tk()
photo = PhotoImage(file="soccer-ball.png")
w = Label(window, image=photo)
w.photo = photo
w.pack()
window.mainloop()