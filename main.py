import pygame
import math
import random
SCREEN_WIDTH= 800
SCREEN_HEIGHT=500
PLAYER_START_X=370
PLAYER_START_Y=380
ENEMY_START_Y_MIN=50
ENEMY_START_Y_MAX=150
ENEMY_SPEED_X=4
ENEMY_SPEED_Y=40
BULLET_SPEED_Y=10
COLLISION_DISTANCE=27
pygame.init()
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
Background=pygame.image.load('background.jpg')
pygame.display.set_caption('Space invader')
icon=pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
playerimg=pygame.image.load('player.png')
playerX=PLAYER_START_X
playerY=PLAYER_START_Y
playerX_change=0
enemy_img=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_ememies=6