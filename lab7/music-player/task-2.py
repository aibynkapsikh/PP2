import pygame

pygame.init()

pygame.mixer.init()

playlist = ["labs/lab7/music-player/music/song1.mp3", 
            "labs/lab7/music-player/music/song2.mp3",
             "labs/lab7/music-player/music/song3.mp3"]
current_song = 0

def play_song():
    pygame.mixer.music.load(playlist[current_song])
    pygame.mixer.music.play()
            
play_song()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_s: 
                pygame.mixer.music.stop()
            elif event.key == pygame.K_RIGHT:  
                current_song = (current_song + 1) % len(playlist)
                play_song()
            elif event.key == pygame.K_LEFT:  
                current_song = (current_song - 1) % len(playlist)
                play_song()

pygame.quit()
