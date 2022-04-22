import sys
import pygame
import math
import os
from pygame.locals import *
from sys import exit
import time as T
from random import *
from pygame.locals import *
pygame.init()
pygame.mixer.init()
BGM = pygame.mixer.Sound('./music/HOTEL CALIFORNIA BGM.mp3')
BGM.play(-1)
background_image="./picture/微信图片_20211107200916.jpeg"
qiuyingxu001 = pygame.image.load("./picture/仇应许0.01.jpg")
matianzuo001=pygame.image.load("./picture/马天佐0.01.jpg")
kuang = pygame.image.load("./picture/btn_prev_h.png")
ft = pygame.font.Font("./Fonts/simkai.ttf", 40)
text1 = ft.render("仇应许v小，", True, (225,225,225))
text2 = ft.render("火力强；", True, (225,225,225))
text3 = ft.render("马天佐v大，", True, (225,225,225))
text4 = ft.render("火力弱.", True, (225,225,225))
text5 = ft.render("按q选择仇应许",True,(225,225,225))
text6 = ft.render("按m选择马天佐",True,(225,225,225))
text7 = ft.render("你只有一次机会",True,(225,225,225))
screen = pygame.display.set_mode((1500,750))
screen.blit(qiuyingxu001,[50,50])
screen.blit(matianzuo001,[600,50])
screen.blit(text1,[1100,50])
screen.blit(text2,[1100,100])
screen.blit(text3,[1100,150])
screen.blit(text4,[1100,200])
screen.blit(text5,[1100,250])
screen.blit(text6,[1100,300])
screen.blit(text7,[1100,350])
pygame.display.flip()
pygame.display.update()
while True:
    	for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_q:
                    BGM.stop()
                    os.system("python ./q.py")
                    exit()
                if event.key == K_m:
                    BGM.stop()
                    os.system("python ./m.py")
                    exit()
