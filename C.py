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
ft = pygame.font.Font("./Fonts/simkai.ttf", 40)
text8 = ft.render("东方永数抄　～ Imperishable Maths. 为校园弹幕射击游戏", True, (225,225,225))
text9 = ft.render("这次，平凡，是以之前从未有过的强大敌人为对手______虽然没有之前什么的",True,(225,225,225))
text11 = ft.render("马天佐与仇的数学课代表两位，来解决某个异变",True,(225,225,225))
text10 = ft.render("就异变来说应许",True,(225,225,225))
text12 = ft.render("两个悠闲的人类开始行动了", True, (225,225,225))
text13 = ft.render("看清传统的高速移动_悠闲的马天佐,与低速移动_悠",True,(225,225,225))
text14 = ft.render("闲的仇应许,的两人的性格的不同",True,(225,225,225))
text15 = ft.render("看破幻想或无视幻想,躲避弹幕或观察弹幕的同时收集分数吧",True,(225,225,225))
text16 = ft.render("虚幻的数学之夜的命运，交给了悠闲的同学们的手中--不", True, (225,225,225))
text17 = ft.render("过，这样好吗，真的好吗",True,(225,225,225))
text18 = ft.render("按c继续",True,(225,225,225))
while True:
        screen = pygame.display.set_mode((1500,750))
        screen.blit(text8,[50,50])
        screen.blit(text9,[50,100])
        screen.blit(text10,[50,150])
        screen.blit(text11,[50,200])
        screen.blit(text12,[50,250])
        screen.blit(text13,[50,300])
        screen.blit(text14,[50,350])
        screen.blit(text12,[50,250])
        screen.blit(text13,[50,300])
        screen.blit(text14,[50,350])
        screen.blit(text15,[50,400])
        screen.blit(text16,[50,450])
        screen.blit(text17,[50,500])
        screen.blit(text18,[50,550])
        pygame.display.flip()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_c:
                    BGM.stop()
                    os.system("python ./a.py")
                    exit()
                                    