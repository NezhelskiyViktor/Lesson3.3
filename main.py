"""
Разработка игры "Тир" на базе урока OG03
"""
import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
pygame.display.set_caption('Игра Тир')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
icon = pygame.image.load('images/icon.jpg')
pygame.display.set_icon(icon)
target_image = pygame.image.load('images/00_00001553_1-800x800.jpg')
target_width = 200
target_height = 200
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))



running = True
while running:
    pass

pygame.quit()
