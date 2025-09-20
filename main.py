#  Осталось проверить, не лежит ли точка (event.x, event.y) дальше,
# чем r от точки (x,y).
# Для этого, с помощью теоремы Пифагора мы найдем расстояние между двумя точками
# и сравним с радиусом круга.

import pygame
from math import sqrt
from pygame.draw import * # type: ignore
from random import randint
pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 800))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    global x, y, r
    '''рисует новый шарик '''
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def click(event):
    print(x, y)
    # координаты клика мыши
    (mx, my) = pygame.mouse.get_pos()
    print(mx, my)
    # расчет расстояния от точки клика до центра шара
    s = sqrt((mx-x)**2+(my-y)**2)
    if s < r:
        screen.fill(BLUE)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)

    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
