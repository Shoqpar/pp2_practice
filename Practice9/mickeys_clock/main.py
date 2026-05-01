import pygame
import datetime
import math

pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey's Clock")
clock = pygame.time.Clock()

def rotate_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)
    return rotated_image, new_rect

try:
    left_hand_img = pygame.image.load('images/left_hand.png') 
    right_hand_img = pygame.image.load('images/right_hand.png')
except FileNotFoundError:
    print("Ошибка: Не найдены изображения в папке images/. Добавь left_hand.png, right_hand.png")
    pygame.quit()
    exit()

center_x, center_y = WIDTH // 2, HEIGHT // 2
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = datetime.datetime.now()
    second = current_time.second
    minute = current_time.minute

    sec_angle = -second * 6
    min_angle = -minute * 6

    screen.fill((255, 255, 255))

    rotated_min, min_rect = rotate_center(right_hand_img, min_angle, center_x, center_y)
    screen.blit(rotated_min, min_rect)

    rotated_sec, sec_rect = rotate_center(left_hand_img, sec_angle, center_x, center_y)
    screen.blit(rotated_sec, sec_rect)

    pygame.display.flip()
    clock.tick(60) 

pygame.quit()