"""
Разработка игры "Тир" на базе урока OG03
"""
import pygame
import random


pygame.init()

FPS = 40
clock = pygame.time.Clock()
# Скорость и направление
speed = [1, -1]

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
target_rect = target_img.get_rect()
target_centr_x, target_centr_y = target_rect.width // 2, target_rect.height // 2
target_pos = (SCREEN_W_MAX // 2, SCREEN_H_MAX // 2)

hole_img = pygame.image.load('images/hole1.png').convert_alpha()
hole_rect = hole_img.get_rect()
hole_centr_x, hole_centr_y = hole_rect.width // 2, hole_rect.height // 2
hole_pos = (0, 0)
hole_show = False
print(hole_rect.width)

dx, dy = 0, 0

main_font = pygame.font.Font('font/font.ttf', 65)
font = pygame.font.Font('font/font.ttf', 18)
title_record = font.render('record:', True, pygame.Color('purple'))

# color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
color = (255, 255, 255)
record = ''
zone = 0


def score_per_shot(hole_, target):
    return 10 - int(pow(((target[0] + target_centr_x - hole_[0]) ** 2
                         + (target[1] + target_centr_y - hole_[1]) ** 2), 0.5) / hole_rect.width)


screen.blit(target_img, target_pos)

while True:
    screen.fill(color)
    target_rect = target_rect.move(speed)
    hole_rect = hole_rect.move(speed)
    target_pos = (target_rect.left + target_rect.right) // 2, (target_rect.top + target_rect.bottom) // 2
    hole_pos = (hole_rect.left + hole_rect.right) // 2, (hole_rect.top + hole_rect.bottom) // 2
    if target_pos[0] < 0 or target_pos[0] > SCREEN_W_MAX:
        speed[0] = -speed[0]
    if target_pos[1] < 0 or target_pos[1] > SCREEN_H_MAX:
        speed[1] = -speed[1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            hole_pos = mouse_pos[0] - random.randint(2, 16), mouse_pos[1] - random.randint(2, 16)
            zone = score_per_shot(hole_pos, target_pos)
            hole_show = True
            record = f'Попадание в {zone}' if zone > 0 else 'Мимо'
            dx = hole_pos[0] - hole_centr_x - target_pos[0]
            dy = hole_pos[1] - hole_centr_y - target_pos[1]

    screen.blit(target_img, target_pos)
    if hole_show:
        hole_pos = target_pos[0] + dx, target_pos[1] + dy
        screen.blit(hole_img, hole_pos)
    screen.blit(font.render(record, True, pygame.Color('black')), (40, 50))
    pygame.display.flip()
    clock.tick(FPS)

