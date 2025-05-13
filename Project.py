import pygame
from pygame.locals import *
import time
import datetime

pygame.init()
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption("Physical Files")
page=0

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                page+=1
            if event.key == K_LEFT:
                page-=1