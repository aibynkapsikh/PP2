import pygame

pygame.init

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pygame KBTU")
icon = pygame.image.load('myself/pygame/images/icon.webp')
pygame.display.set_icon(icon)
pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))

is_blue = True
x = 30
y = 30

clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = False
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3

    screen.fill((0, 0, 0))
    if not is_blue: color = (0, 128, 255)
    else: color = (255, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

    pygame.display.flip()
    clock.tick(60)
        


