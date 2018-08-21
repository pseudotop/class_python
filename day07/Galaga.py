from tkinter import *

class Bullet:
    bullet_list = []
    def __init__(self,canvas,x,y):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.img_bullet = PhotoImage(file='img/bullet.png')
        self.me = self.canvas.create_image(self.x, self.y, image=self.img_bullet)
        Bullet.bullet_list.append(self)

    def move(self):
        self.canvas.move(self.me, 0, -5)
        self.y += -5
        if self.y < 10:
            self.canvas.delete(self.me)
            Bullet.bullet_list.remove(self)

class Ship:
    def __init__(self, canvas):
        self.x = 385
        self.y = 560
        self.dx, self.dy = 0,0 # 키가 눌리면 abs(dx),abs(dy) = 5
        self.canvas = canvas
        self.img_ship = PhotoImage(file='img/ship.png')
        self.me = self.canvas.create_image(self.x, self.y, image=self.img_ship)

    def move_left(self,event):
        if(self.x <= 0):
            return
        self.canvas.move(self.me,-5,0)
        self.x += -5
    def move_right(self,event):
        if(self.x >= 785):
            return
        self.canvas.move(self.me,5,0)
        self.x += 5

    def shoot(self,event):
        Bullet(self.canvas,self.x,self.y)

class Enemy:
    enemy_list = []
    def __init__(self,canvas,x,y):
        self.x = x
        self.y = y
        self.width, self.height = 20, 20
        self.canvas = canvas
        self.img_enemy = PhotoImage(file='img/enermy1.png')
        self.me = self.canvas.create_image(self.x, self.y, image=self.img_enemy)
        Enemy.enemy_list.append(self)
    def check_collision(self,bullet):
        my_x1 = self.x
        my_x2 = self.x + self.width
        my_y = self.y + self.height

        bullet_x1 = bullet.x
        bullet_x2 = bullet.x + 20
        bullet_y  = bullet.y

        if(my_y > bullet_y and \
            ((my_x1 < bullet_x1 and my_x2 > bullet_x1) or \
            (my_x1 < bullet_x2 and my_x2 > bullet_x2))  \
        ):
            print('collision')
            self.canvas.delete(self.me)
            Enemy.enemy_list.remove(self)
            self.canvas.delete(bullet.me)
            Bullet.bullet_list.remove(bullet)

class App:
    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas(self.window, width=800, height=600)
        self.canvas.pack()
        self.ship = Ship(self.canvas)
        for y in range(0, 2):
            for x in range(0, 12):
                enemy = Enemy(self.canvas,100+ (x*50), 50 + y*30)
        # self.bg = PhotoImage('img/bg.png')
        # self.canvas.create_image(0,0,image=self.bg)

    def bind_event(self):
        self.window.bind('<KeyPress-Left>',self.ship.move_left)
        self.window.bind('<KeyPress-Right>',self.ship.move_right)
        self.window.bind('<KeyPress-space>',self.ship.shoot)

    def loop(self):
        for bullet in Bullet.bullet_list:
            bullet.move()
        for enemy in Enemy.enemy_list:
            for bullet in Bullet.bullet_list:
                enemy.check_collision(bullet)
        self.window.after(10, self.loop)

game = App()
game.bind_event()
game.loop()
game.window.mainloop()
