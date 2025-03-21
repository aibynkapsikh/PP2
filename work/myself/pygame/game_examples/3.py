import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Game, so but")
icon = pygame.image.load('myself/pygame/images/icon.webp')
pygame.display.set_icon(icon)

square = pygame.Surface((50, 100))
square.fill('Green')

myfont = pygame.font.Font('myself/pygame/fonts/BebasNeue-Regular.ttf', 50)
text_surface = myfont.render('Aibyn', True, 'White')

player = pygame.image.load('myself/pygame/images/piece.jpg')
player = pygame.transform.scale(player, (300, 200))

player_x = 30
player_y = 30
running = True
while running:

    screen.fill((118, 100, 91))
    pygame.draw.circle(square, 'Red', (15, 40), 3)
    screen.blit(square, (70, 70))
    screen.blit(text_surface, (300, 310))  
    screen.blit(player, (player_x, player_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= 10
            if event.key == pygame.K_RIGHT:
                player_x += 10
            if event.key == pygame.K_UP:
                player_y -= 10
            if event.key == pygame.K_DOWN:
                player_y += 10
            
    pygame.display.update()