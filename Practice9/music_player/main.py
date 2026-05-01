import pygame
import os

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 600, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")
font = pygame.font.SysFont("consolas", 24)

music_dir = "music"
tracks = []
if os.path.exists(music_dir):
    tracks = [f for f in os.listdir(music_dir) if f.endswith(('.mp3', '.wav'))]

current_track_idx = 0
is_playing = False

if tracks:
    pygame.mixer.music.load(os.path.join(music_dir, tracks[current_track_idx]))

def draw_ui():
    screen.fill((30, 30, 30))
    if not tracks:
        text = font.render("No tracks found in 'music/' folder", True, (255, 100, 100))
        screen.blit(text, (20, HEIGHT // 2))
        return

    track_name = tracks[current_track_idx]
    track_text = font.render(f"Now: {track_name}", True, (200, 200, 200))
    
    status_str = "PLAYING" if is_playing else "STOPPED/PAUSED"
    status_color = (100, 255, 100) if is_playing else (255, 100, 100)
    status_text = font.render(f"Status: {status_str}", True, status_color)
    
    controls_text = font.render("Controls: [P]lay/Pause | [S]top | [N]ext | [B]ack | [Q]uit", True, (150, 150, 150))

    screen.blit(track_text, (20, 50))
    screen.blit(status_text, (20, 100))
    screen.blit(controls_text, (20, 200))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            
            if not tracks: 
                continue

            # P - Play / Pause
            if event.key == pygame.K_p:
                if is_playing:
                    pygame.mixer.music.pause()
                    is_playing = False
                else:
                    pygame.mixer.music.unpause() if pygame.mixer.music.get_pos() > 0 else pygame.mixer.music.play()
                    is_playing = True
            
            # S - Stop
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                is_playing = False
            
            # N - Next
            elif event.key == pygame.K_n:
                current_track_idx = (current_track_idx + 1) % len(tracks)
                pygame.mixer.music.load(os.path.join(music_dir, tracks[current_track_idx]))
                pygame.mixer.music.play()
                is_playing = True
                
            # B - Previous (Back)
            elif event.key == pygame.K_b:
                current_track_idx = (current_track_idx - 1) % len(tracks)
                pygame.mixer.music.load(os.path.join(music_dir, tracks[current_track_idx]))
                pygame.mixer.music.play()
                is_playing = True

    draw_ui()
    pygame.display.flip()

pygame.quit()