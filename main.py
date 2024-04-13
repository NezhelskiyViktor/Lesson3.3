"""
Разработка игры "Тир" на базе урока OG03
"""
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
pygame.display.set_caption('Игра Тир')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
icon = pygame.image.load('images/icon.jpg')

running = True
while running:
    pass

pygame.quit()
