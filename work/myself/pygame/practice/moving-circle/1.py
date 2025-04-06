import pygame
import time

pygame.init()

blue = (0, 0, 255)

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Moving Circle")

clock = pygame.time.Clock()
last_move_time = time.time()
x = 200
y = 300

running = True

while running:

    screen.fill((255, 255, 255))
    circle = pygame.draw.circle(screen, blue, (x, y), 12)

    if time.time() - last_move_time >= 1:

        x += 10
        last_move_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
