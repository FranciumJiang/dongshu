#start
import os
import sys
import sys
import pygame
import math
import os
from pygame.locals import *
from sys import exit
import time as T
from random import *
from pygame.locals import *
from moviepy.editor import *
print("Would you like to start the game or have a view of Credits")
print("开始游戏，抑或是查看制作人员名单？")
print("Enter S to start game ; Enter V to have a view of Credits")
print("输入S，开始游戏;输入V，查看制作人员名单")
b = input(">:")
if b == 'S':
	print("English,print E ; 中文，输入C")
	a = input("Language 语言？:")
	if a == 'C':
		os.system("python ./C.py")
	elif a == 'E':
		os.system("python ./E.py")
	else:
		print("We have not finished that.")
elif b == 'V':
    pygame.display.set_caption('Credits')
    exitFlag = False
    FPS = 20
    clip = VideoFileClip('生.flv')
    clip.preview()
    pygame.quit()
