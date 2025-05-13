import pygame
from pygame.locals import *
import time
import datetime

pygame.init()
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption("Physical Files")

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()