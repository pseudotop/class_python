from tkinter import *
import random

MAX_RECT = 2
def movingRect(*recti,dx,dy):
    if(canvas.coords(recti)[2]>=canvas.winfo_width() or canvas.coords(recti)[0]<=0):
        dx = -dx
    elif(canvas.coords(recti)[3]>=canvas.winfo_height() or canvas.coords(recti)[1]<=0):
        dy = -dy
    for i in range(MAX_RECT):
        canvas.move(recti,dx,dy)
        if(rect_coord[i]==tuple(canvas.coords(recti))):
            print('continue')
            continue

        # recti : xf
        if(rect_coord[i][2]>=canvas.coords(recti)[2]>=rect_coord[i][0]):
            # recti : yf
            if(rect_coord[i][3]>=canvas.coords(recti)[3]>=rect_coord[i][1]):
                print('xf-yf collision')
                dy = -dy
                continue
            # recti : yi
            if(rect_coord[i][3]>=canvas.coords(recti)[1]>=rect_coord[i][1]):
                print('xf-yi collision')
                dy = -dy
                continue
            print('1. basis state')

        # recti : xi
        if(rect_coord[i][2]>=canvas.coords(recti)[0]>=rect_coord[i][0]):
            # recti : yf
            if(rect_coord[i][3]>=canvas.coords(recti)[3]>=rect_coord[i][1]):
                dy = -dy
                print('xi-yf collision')
                continue
            # recti : yi
            if(rect_coord[i][3]>=canvas.coords(recti)[1]>=rect_coord[i][1]):
                dy = -dy
                print('xi-yi collision')
                continue
            print('2. basis state')

        # recti : yf
        if(rect_coord[i][3]>=canvas.coords(recti)[3]>=rect_coord[i][1]):
            # recti : xf
            if(rect_coord[i][2]>=canvas.coords(recti)[2]>=rect_coord[i][0]):
                print('xf-yf collision')
                dx = -dx
                continue
            # recti : xi
            if(rect_coord[i][2]>=canvas.coords(recti)[0]>=rect_coord[i][0]):
                print('xi-yf collision')
                dx = -dx
                continue
            print('3. basis state')

        # recti : yi
        if(rect_coord[i][3]>=canvas.coords(recti)[1]>=rect_coord[i][1]):
            # recti : xf
            if(rect_coord[i][2]>=canvas.coords(recti)[2]>=rect_coord[i][0]):
                print('xf-yi collision')
                dx = -dx
                continue
            # recti : xi
            if(rect_coord[i][2]>=canvas.coords(recti)[0]>=rect_coord[i][0]):
                print('xi-yi collision')
                dx = -dx
                continue
            print('4. basis state')
        else :
            print('5. basis state')

    canvas.move(recti,dx,dy)
    return (dx,dy)

def startTimer():
    if(running):
        global timer
        global dx, dy
        timer += 1
        for i in range(MAX_RECT):
            dx[i],dy[i]=movingRect(rect[i],dx=dx[i],dy=dy[i])
    window.after(10, startTimer)

def start():
    global running
    running = True

def stop():
    global running
    running = False

def reset():
    global running
    running = False
    for i in range(MAX_RECT):
        canvas.coords(rect[i],*rect_coord[i])

running = False

window = Tk()
timer = 0
rect = []
rect_coord = []
dx = []
dy = []

canvas = Canvas(window, width="600", height="400")
canvas.pack()
for i in range(MAX_RECT):
    x_i = random.randint(10, 500)
    x_f = random.randint(x_i,x_i+100)
    y_i = random.randint(10, 400)
    y_f = random.randint(y_i,y_i+100)
    rect_coord.append((x_i,y_i,x_f,y_f))
    rect.append(canvas.create_rectangle(*rect_coord[-1],fill='pink'))
    # dx.append(random.randint(1,5))
    # dy.append(random.randint(1,5))
    dx.append(1)
    dy.append(1)


startButton = Button(window, text="시작",bg="yellow",command=start)
startButton.pack(fill=BOTH)
stopButton = Button(window, text="중지",bg="yellow",command=stop)
stopButton.pack(fill=BOTH)
resetButton = Button(window, text="리셋",bg="yellow",command=reset)
resetButton.pack(fill=BOTH)

startTimer()
window.mainloop()
