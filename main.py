# Чтобы определить, попали ли мы в круг, 
# нужно знать его координаты, радиус круга и координаты мыши в момент щелчка. Координаты мыши легко получить через event.pos. 
# Попробуем получить координаты круга:

import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
# Использование global – это не самое лучшее решение. 
# Для данной задачи больше подходит использование ООП (объектно-ориентированного подхода), 
# но об этом позже. А пока – будем использовать global.

# global означает, что переменные будут считаться глобальными (а не локальными), 
# т.е. их значение сохранится и после завершения работы функции, 
# а не будет уничтожено, как это произойдет со всеми локальными переменными.
    global x, y, r
    '''рисует новый шарик '''
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    
def click(event):
    print(x, y, r)

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
