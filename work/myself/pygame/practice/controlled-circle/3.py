import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Controlled circle")

x = 300
y = 200

color = (67, 157, 171)

running = True

while running:

    screen.fill((255, 255 , 255))
    pygame.draw.circle(screen, color, (x, y), 12)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 10
            elif event.key == pygame.K_RIGHT:
                x += 10
            elif event.key == pygame.K_DOWN:
                y += 10
            elif event.key == pygame.K_UP:
                y -= 10

    pygame.display.update()

pygame.quit()