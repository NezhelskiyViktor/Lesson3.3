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
TARGET_W = 400
TARGET_H = 400
SCREEN_W_MAX = SCREEN_WIDTH - TARGET_W
SCREEN_H_MAX = SCREEN_HEIGHT - TARGET_H

pygame.display.set_caption('Игра Тир')
icon = pygame.image.load('images/icon.jpg')
pygame.display.set_icon(icon)

target_img = pygame.image.load('images/target400x400.jpg')
target_pos = (SCREEN_W_MAX // 2, SCREEN_H_MAX // 2)

# color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
color = (255, 255, 255)


def score_per_shot(mouse, target):
    return 10 - int(pow(((target[0] + 200 - mouse[0]) ** 2
                         + (target[1] + 200 - mouse[1]) ** 2), 0.5) / 20)


screen.blit(target_img, target_pos)

while True:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(f'{score_per_shot(mouse_pos, target_pos)}')
        #     if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
        #         target_x = random.randint(0, SCREEN_WIDTH - target_width)
        #         target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    screen.blit(target_img, target_pos)

    pygame.display.flip()
#    clock.tick(FPS)

