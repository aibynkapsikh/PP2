import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Traffic Light")

red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)

current_color = red
running = True

while running:

    screen.fill(current_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                current_color = red
            elif event.key == pygame.K_g:
                current_color = green
            elif event.key == pygame.K_y:
                current_color = yellow

    pygame.display.update()

pygame.quit()