import random
import pygame
pygame.init()
player_x=400
player_y=50
screen=pygame.display.set_mode((800,500))
background=pygame.image.load('background.jpg')
pygame.display.set_caption('Space invader')
playerimg=pygame.image.load('player.png')

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

enemies = []
for _ in range(7):
    enemy_x = random.randint(0, 736)
    enemy_y = random.randint(50, 150)
    enemies.append(Enemy(enemy_x, enemy_y))

player_x = random.randint(0, 736)
player_y = random.randint(400, 450)
player = Player(player_x, player_y)
