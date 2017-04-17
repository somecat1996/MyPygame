import pygame
import math
import sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("The Pie Game - Press 1, 2, 3, 4")
myfont = pygame.font.Font(None, 60)

color = 200, 80, 60
width = 4
x = 300
y = 250
radius = 200
position = x - radius, y - radius, radius*2, radius*2

piece1 = False
piece2 = False
piece3 = False
piece4 = False

textImage1 = myfont.render("1", True, color)
textImage2 = myfont.render("2", True, color)
textImage3 = myfont.render("3", True, color)
textImage4 = myfont.render("4", True, color)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_1:
                if piece1:
                    piece1 = False
                else:
                    piece1 = True
            elif event.key == pygame.K_2:
                if piece2:
                    piece2 = False
                else:
                    piece2 = True
            elif event.key == pygame.K_3:
                if piece3:
                    piece3 = False
                else:
                    piece3 = True
            elif event.key == pygame.K_4:
                if piece4:
                    piece4 = False
                else:
                    piece4 = True

    screen.fill((0, 0, 200))

    screen.blit(textImage1, (x + radius / 2 - 20, y - radius / 2))
    screen.blit(textImage2, (x - radius / 2 - 20, y - radius / 2))
    screen.blit(textImage3, (x - radius / 2 - 20, y + radius / 2))
    screen.blit(textImage4, (x + radius / 2 - 20, y + radius / 2))

    if piece1:
        start_angle = math.radians(0)
        end_angle = math.radians(90)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x + radius, y), width)
        pygame.draw.line(screen, color, (x, y), (x, y - radius), width)
    if piece2:
        start_angle = math.radians(90)
        end_angle = math.radians(180)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x - radius, y), width)
        pygame.draw.line(screen, color, (x, y), (x, y - radius), width)
    if piece3:
        start_angle = math.radians(180)
        end_angle = math.radians(270)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x - radius, y), width)
        pygame.draw.line(screen, color, (x, y), (x, y + radius), width)
    if piece4:
        start_angle = math.radians(270)
        end_angle = math.radians(360)
        pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x + radius, y), width)
        pygame.draw.line(screen, color, (x, y), (x, y + radius), width)

    if piece1 and piece2 and piece3 and piece4:
        color = 0, 255, 0
    else:
        color = 200, 80, 60

    pygame.display.update()