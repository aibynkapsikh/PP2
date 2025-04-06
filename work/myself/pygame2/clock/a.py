import pygame
import time
from datetime import datetime

pygame.init()

clock_img = pygame.image.load('labs/lab7/clock/pictures/mouse.png')
min_hand = pygame.image.load('labs/lab7/clock/pictures/min.png')
sec_hand = pygame.image.load('labs/lab7/clock/pictures/sec.png')

width, height = clock_img.get_size()

CENTER = (width / 2, height / 2)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Clock")

def rotate_image(image, angle):
    rotated_image = pygame.transform.rotate(image, -angle)
    rect = rotated_image.get_rect(center=CENTER)
    return rotated_image, rect

running = True

while running:
    screen.fill((255, 255, 255))
    screen.blit(clock_img, (0, 0))

    now = datetime.now()
    minute = now.minute * 6
    second = now.second * 6

    rotated_minute, min_rect = rotate_image(min_hand, minute)
    rotated_second, sec_rect = rotate_image(sec_hand, second)

    screen.blit(rotated_minute, min_rect.topleft)
    screen.blit(rotated_second, sec_rect.topleft)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time.sleep(1)

pygame.quit()


