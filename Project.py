import pygame
from pygame.locals import *
import time
import datetime

class Object:
    def __init__(self,x,y,scaleX,scaleY,sFactors):
        self.x=x
        self.y=y
        self.scaleX=scaleX
        self.scaleY=scaleY
        self.sFactors=sFactors

    def scaleUp(self):
        global page
        self.scaleX*=self.sFactors[page]
        self.scaleY*=self.sFactors[page]
    
    def scaleDown(self):
        global page
        self.scaleX=self.scaleX/self.sFactors[page]
        self.scaleY=self.scaleY/self.sFactors[page]

pygame.init()
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption("Physical Files")
page=1
test=Object(100,100,1,1,[1,1.3,2,1.5])

def toInt(num):
    return int(num//1)

while True:
    pygame.draw.rect(screen,"red",(test.x,test.y,toInt(100*test.scaleX),toInt(100*test.scaleY)),toInt(100*max(test.scaleX,test.scaleY)))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                if page<4:
                    test.x+=100
                    test.scaleUp()
                    page+=1
            if event.key == K_LEFT:
                if page>0:
                    page-=1
                    test.scaleDown()
                    test.x-=100
    pygame.display.update()
    screen.fill("black")
