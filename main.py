"""
Разработка игры "Тир" на базе урока OG03
"""
import pygame
import random
import math


pygame.init()
pygame.mouse.set_visible(False)

FPS = 150
clock = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Игра Тир')
icon = pygame.image.load('images/icon.jpg')
pygame.display.set_icon(icon)

# Мишень
target_img = pygame.image.load('images/target400x400.jpg')
target_rect = target_img.get_rect()
# # Скорость и направление движения мишени
# speed = [1, 1]
# # Граница перемещения мишени
# edge_right = SCREEN_WIDTH - target_rect.width
# edge_bottom = SCREEN_HEIGHT - target_rect.height

# Дырки
hole_img = pygame.image.load('images/hole1.png').convert_alpha()
hole_rect = hole_img.get_rect()
hole_list = []

# Прицел
aim_img = pygame.image.load('images/aim.png').convert_alpha()
aim_rect = aim_img.get_rect()

font = pygame.font.Font('font/font.ttf', 18)

record = ''
zone = 0
# Новые переменные для синусоидального движения
x = -400  # Начальная позиция по оси X
amplitude = 100  # Амплитуда синусоиды
frequency = 0.01  # Частота синусоиды


def score_per_shot(hole_, target):
    res = (10 - int(((target[0] + target_rect.width // 2 - hole_[0]) ** 2
                     + (target[1] + target_rect.height // 2 - hole_[1]) ** 2)
                    ** 0.5) // hole_rect.width)
    return res


target_rect = target_rect.move((0, -100))
while True:
    aim_rect.center = pygame.mouse.get_pos()
    screen.fill(pygame.Color('white'))

    # Обновляем позицию мишени для движения слева направо по синусоидальной траектории
    # Вычисляем Y используя синусоиду
    y = SCREEN_HEIGHT // 2 + math.sin(frequency * x) * amplitude - target_rect.height // 2
    target_pos = (x, y)
    x += 2  # Увеличиваем X для следующего кадра
    if x > SCREEN_WIDTH:  # Если мишень достигла края экрана, начинаем снова
        x = -400
        hole_list = []

    # target_rect = target_rect.move(speed)
    # target_pos = ((target_rect.left + target_rect.right) // 2,
    #               (target_rect.top + target_rect.bottom) // 2)
    # if target_pos[0] < 0 or target_pos[0] > edge_right:
    #     speed[0] = -speed[0]
    # if target_pos[1] < 0 or target_pos[1] > edge_bottom:
    #     speed[1] = -speed[1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # позицию дырки определяем по положению курсора с небольшим разбросом
            hole_pos = (mouse_pos[0] - random.randint(-4, 5),
                        mouse_pos[1] - random.randint(-4, 5))
            hole_list.append((hole_pos[0] - hole_rect.center[0] - target_pos[0],
                              hole_pos[1] - hole_rect.center[1] - target_pos[1]))
            zone = score_per_shot(hole_pos, target_pos)
            record = f'Попадание в {zone}' if zone > 0 else 'Мимо'

    screen.blit(target_img, target_pos)
    for pos in hole_list:  # для всех дырок на мишени
        screen.blit(hole_img, (target_pos[0] + pos[0], target_pos[1] + pos[1]))
    screen.blit(font.render(record, True, pygame.Color('black')), (10, 10))
    screen.blit(aim_img, aim_rect)
    pygame.display.flip()
    clock.tick(FPS)
