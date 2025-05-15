import pygame
from pygame.locals import *
import time
import datetime

class object:
    def __init__(self,x,y,scalex,scaley):
        self.x=x
        self.y=y
        self.scalex=scalex
        self.scaley=scaley

pygame.init()
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption("Physical Files")
page=0
test=object(100,100,1,1)

while True:
    pygame.draw.rect(screen,"red",(test.x,test.y,100*test.scalex,100*test.scaley),100)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                page+=1
                test.x+=100
                test.scalex*=1.1
                test.scaley*=1.1
            if event.key == K_LEFT:
                page-=1
                test.x-=100
                test.scalex/=1.1
                test.scaley/=1.1
    pygame.display.update()
    screen.fill("black")
