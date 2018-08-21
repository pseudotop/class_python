import pygame
import math
import random

pygame.init()

width, height = 640,480
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width,height))
playerpos = [100,100]
keys = dict()
keys['w'] = False
keys['a'] = False
keys['s'] = False
keys['d'] = False
bullets = []
badguys = []
badtimer = 100
imove = 0

player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
bullet = pygame.image.load("resources/images/bullet.png")
badguy = [
    pygame.image.load("resources/images/badguy.png"),
    pygame.image.load("resources/images/badguy2.png"),
    pygame.image.load("resources/images/badguy3.png"),
    pygame.image.load("resources/images/badguy4.png")
]

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keys['w'] = True
                pass
            if event.key == pygame.K_a:
                keys['a'] = True
                pass
            if event.key == pygame.K_s:
                keys['s'] = True
                pass
            if event.key == pygame.K_d:
                keys['d'] = True
                pass
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys['w'] = False
                pass
            if event.key == pygame.K_a:
                keys['a'] = False
                pass
            if event.key == pygame.K_s:
                keys['s'] = False
                pass
            if event.key == pygame.K_d:
                keys['d'] = False
                pass
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(event.button == 1):
                m_pos = pygame.mouse.get_pos()
                b = [ math.atan2(m_pos[1] - playerpos[1],m_pos[0] - playerpos[0]),
                      playerpos[0], playerpos[1]]
                bullets.append(b)
            if(event.button == 3):
                m_pos = pygame.mouse.get_pos()
                for i in range(20):
                    j = i
                    if (i<10): j = -j
                    b = [ math.atan2(m_pos[1] - playerpos[1] + 5*j,m_pos[0] - playerpos[0]),
                          playerpos[0], playerpos[1]]
                    bullets.append(b)


    if keys['w']:
        playerpos[1] -= 5
    if keys['a']:
        playerpos[0] -= 5
    if keys['s']:
        playerpos[1] += 5
    if keys['d']:
        playerpos[0] += 5

    m_pos = pygame.mouse.get_pos()
    angle = math.atan2(m_pos[1] - playerpos[1], m_pos[0] - playerpos[0])
    player_rotate = pygame.transform.rotate(player, 360-angle*(180/math.pi))

    for b in bullets:
        index = 0
        velx = math.cos(b[0]) * 10
        vely = math.sin(b[0]) * 10
        b[1] += velx
        b[2] += vely

        if b[2] < 0 or b[2] > height or b[1] < 0 or b[1] > width:
            bullets.pop(index)
        index += 1

    badtimer -= 1
    if badtimer == 0:
        badguys.append([640, random.randint(50, 430)])
        badtimer = random.randint(70, 100)

    index = 0
    for bg in badguys:
        if bg[0] < 0:
            badguys.pop(index)
        bg[0] -= 5

        print(index)
        badrect = pygame.Rect(badguy[imove].get_rect())
        badrect.left = bg[0]
        badrect.top = bg[1]
        index1 = 0
        is_kill = False
        for b in bullets:
            b_rect = pygame.Rect(bullet.get_rect())
            b_rect.left = b[1]
            b_rect.top = b[2]
            if badrect.colliderect(b_rect):
                if not is_kill:
                    badguys.pop(index)
                bullets.pop(index1)
                is_kill = True
            index1 += 1

        index += 1

    screen.fill((0, 0, 0))
    for x in range(width // grass.get_width() + 1):
        for y in range(height // grass.get_height() + 1):
            screen.blit(grass, (x * 100, y * 100))
    screen.blit(castle, (0, 30))
    screen.blit(castle, (0, 135))
    screen.blit(castle, (0, 240))
    screen.blit(castle, (0, 345))

    if((playerpos[0]<0 or playerpos[0]>width) or (playerpos[1]<0 or playerpos[1]>height)):
        if(playerpos[0]<0): playerpos[0] = 5
        if(playerpos[0]>width - player.get_width()): playerpos[0] = width - player.get_width()
        if(playerpos[1]<0): playerpos[1] = 5
        if(playerpos[1]>height - player.get_height()): playerpos[1] = height - player.get_height()
    for b in bullets:
        b_rotate = pygame.transform.rotate(bullet, 360-b[0]*(180/math.pi))
        screen.blit(b_rotate, (b[1],b[2]))
    screen.blit(player_rotate, playerpos)
    for bg in badguys:
        screen.blit(badguy[imove], (bg[0], bg[1]))
    # playerpos[0] += 10

    if(imove%3 == 0): imove = 0
    imove += 1
    clock.tick(30)
    pygame.display.flip()
