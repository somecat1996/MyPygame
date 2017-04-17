import pygame
import sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Drawing Lines")

start_x = 100
start_y = 100
end_x = 500
end_y = 400
vel_s_x = 0.2
vel_s_y = 0.1
vel_e_x = -0.2
vel_e_y = -0.3

color = 100, 255, 200
width = 2

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill((0, 80, 0))

    start_x += vel_s_x
    start_y += vel_s_y
    end_x += vel_e_x
    end_y += vel_e_y

    if start_y > 500 or start_y < 0:
        vel_s_y = -vel_s_y
    if start_x > 600 or start_x < 0:
        vel_s_x = -vel_s_x
    if end_y > 500 or end_y < 0:
        vel_e_y = -vel_e_y
    if end_x > 600 or end_x < 0:
        vel_e_x = -vel_e_x

    start = start_x, start_y
    end = end_x, end_y

    pygame.draw.line(screen, color, start, end, width)

    pygame.display.update()