import pygame
import sys
pygame.init()

FPS = 60 #
# все значения переменных снизу просто фактически искал по картинке, чтобы анимация легла на фоновый рисунок(paint)
WIN_HEIGHTMAX = 286 # координата макс высота 
WIN_HEIGHTMIN = 168 # координата мин высота
WIN_LENGHTMAX = 580 # координата макс длина
WIN_LENGHTMIN = 249 # координата мин длина

RED = (255, 0, 0) 
ORANGE = (255, 150, 100) 

UP = 'to the up'
DOWN = 'to the down'
LEFT = 'to the left'
RIGHT = 'to the right'

clock = pygame.time.Clock() 

sc = pygame.display.set_mode((916, 482)) 

# размеры и координаты левого угла
side = 6 # у квадрата ширина и высота равны
x = 438# точка начала по x
x1 = 249 #
y = 168 # точка начала по y
angle = 90

background_image = pygame.image.load('amper1.png')
amper2 = pygame.image.load('amper2.png')
myfont = pygame.font.SysFont("monospace", 22)
rect = amper2.get_rect(center=(500, 220))
direction = UP# направление движения
direction1 = LEFT #
pygame.display.set_caption("События от мыши")

flag = 1 # переменная для проверки нажатия кнопки
while 1: # сама программа
    for i in pygame.event.get(): # проверка новых объектов
        if i.type == pygame.QUIT: 
            sys.exit() # выход - анимация перестанет работать, но выходить нужно, закрыв Shell
        elif i.type == pygame.MOUSEBUTTONDOWN: # если нажали кнопку мыши
            flag = (flag + 1) % 2 # меняем четность
    pygame.display.set_caption("Сила Ампера")
    sc.blit(background_image, (0, 0)) # постоянно обновляются
    new_apmp = pygame.transform.rotate(amper2, angle - 90)
    r = new_apmp.get_rect(center=(rect.center[0], rect.center[1]))
    sc.blit(new_apmp, r)
    txt_ = myfont.render(f"угол {angle}", 1, (0, 0, 0))
    sc.blit(txt_, (600, 10))

    pygame.draw.rect(sc, ORANGE, (x, y, side, side)) # квадратики на магнитных линиях
    pygame.draw.rect(sc, ORANGE, (x + 25, y, side, side)) 
    pygame.draw.rect(sc, ORANGE, (x + 59, y, side, side))
    pygame.draw.rect(sc, ORANGE, (x + 90, y, side, side))
    pygame.draw.rect(sc, ORANGE, (x + 115, y, side, side))
    pygame.draw.rect(sc, RED, (x1, 220, side, side)) # квадратики на проводнике - типо ток
    pygame.draw.rect(sc, RED, (x1 + 50, 220, side, side))
    pygame.draw.rect(sc, RED, (x1 + 100, 220, side, side))
    pygame.draw.rect(sc, RED, (x1 + 150, 220, side, side))
    
    # меняем направление, когда сталкиваемся с краями для красоты, можешь переделать
    if y + side >= WIN_HEIGHTMAX: # (y + side) - координата верхней границы квадрата
        direction = DOWN
    elif y <= 168: 
        direction = UP
    if direction == UP: 
        y += 3
    else: # если направление вверх
        y -= 3
    if flag == 0: # если четность поменяли, то делаем справа налево и наоборот  
        if x1 - side <= 249: # 
            direction1 = LEFT
        elif x1 >= 249: 
            direction1 = RIGHT
        if direction1 == RIGHT:
            x1 -= 3
        else: # если дошел до края
            x1 = 580
    else:
        if x1 + side >= WIN_LENGHTMAX: # (y + side) - координата верхней границы квадрата
            direction1 = RIGHT
        elif x1 <= 249: 
            direction1 = LEFT
        if direction1 == LEFT:
            x1 += 3
        else: # если дошел до края
            x1 = 249
    pygame.display.update()
    clock.tick(FPS)

