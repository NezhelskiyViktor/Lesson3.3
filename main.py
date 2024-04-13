"""
Разработка игры "Тир" на базе урока OG03
"""
import pygame
import random


pygame.init()

FPS = 60
clock = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
TARGET_W = 200
TARGET_H = 200
SCREEN_W_MAX = SCREEN_WIDTH - TARGET_W
SCREEN_H_MAX = SCREEN_HEIGHT - TARGET_H

pygame.display.set_caption('Игра Тир')
icon = pygame.image.load('images/icon.jpg')
pygame.display.set_icon(icon)

target_img = pygame.image.load('images/target.jpg')
target_x = SCREEN_W_MAX // 2
target_y = SCREEN_H_MAX // 2

# color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
color = (255, 255, 255)

def move_target(mouse_get_pos):
    target_x = random.randint(0, SCREEN_W_MAX)
    target_y = random.randint(0, SCREEN_H_MAX)


screen.blit(target_img, (target_x, target_y))

while True:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            deviation_from_target = (((mouse_x ** 2) + (mouse_y ** 2))
                                     - ((target_x + 100) ** 2) + ((target_y + 100) ** 2))
            print(f'{10 - int(pow(((target_x + 100 - mouse_x) ** 2 + (target_y + 100 - mouse_y) ** 2), 0.5) / 10)}')
        #     if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
        #         target_x = random.randint(0, SCREEN_WIDTH - target_width)
        #         target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    screen.blit(target_img, (target_x, target_y))

    pygame.display.flip()
#    clock.tick(FPS)

