import pygame

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1000, 650))
pygame.display.set_caption("New game")
icon = pygame.image.load('labs/work/myself/pygame/images/icon.webp')
pygame.display.set_icon(icon)


bg = pygame.image.load('labs/work/myself/pygame/background/bg.jpg')

left_side = [
    pygame.image.load('labs/work/myself/pygame/images/left_side/image.png'),
    pygame.image.load('labs/work/myself/pygame/images/left_side/image copy.png'),
    pygame.image.load('labs/work/myself/pygame/images/left_side/image copy 2.png'),
    pygame.image.load('labs/work/myself/pygame/images/left_side/image copy 3.png')
]
right_side = [
    pygame.image.load('labs/work/myself/pygame/images/right_side/image.png'),
    pygame.image.load('labs/work/myself/pygame/images/right_side/image copy.png'),
    pygame.image.load('labs/work/myself/pygame/images/right_side/image copy 2.png'),
    pygame.image.load('labs/work/myself/pygame/images/right_side/image copy 3.png')
]
player = [
    pygame.image.load('labs/work/myself/pygame/images/right_side/image.png'),
    pygame.image.load('labs/work/myself/pygame/images/right_side/image copy.png'),
    pygame.image.load('labs/work/myself/pygame/images/right_side/image copy 2.png'),
    pygame.image.load('labs/work/myself/pygame/images/right_side/image copy 3.png')
]
player_speed = 5
player_x = 300
player_y = 530

is_jump = False
jump_count = 6
player_anim_count = 0
bg_x = 0

bg_sound = pygame.mixer.Sound('labs/work/myself/pygame/sounds/music.mp3')
# bg_sound.play()
playing = True
while playing:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 1000, 0))
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        screen.blit(left_side[player_anim_count], (player_x, player_y))
    else:
        screen.blit(right_side[player_anim_count], (player_x, player_y))

    if keys[pygame.K_LEFT] and player_x > 50:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < 700:
        player_x += player_speed

    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1

    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -6:
            if jump_count > 0:
                player_y -= (jump_count ** 2)/2
            else:
                player_y += (jump_count ** 2)/2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 6

    bg_x -= 5
    if bg_x == -1000:
        bg_x = 0
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()

    clock.tick(13)

