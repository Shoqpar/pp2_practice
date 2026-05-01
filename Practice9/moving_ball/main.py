import pygame
from ball import RADIUS, BALL_COLOR, BG_COLOR, STEP

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")
clock = pygame.time.Clock()


x, y = WIDTH // 2, HEIGHT // 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y - STEP >= RADIUS:
                    y -= STEP
            elif event.key == pygame.K_DOWN:
                if y + STEP <= HEIGHT - RADIUS:
                    y += STEP
            elif event.key == pygame.K_LEFT:
                if x - STEP >= RADIUS:
                    x -= STEP
            elif event.key == pygame.K_RIGHT:
                if x + STEP <= WIDTH - RADIUS:
                    x += STEP

    screen.fill(BG_COLOR)
    pygame.draw.circle(screen, BALL_COLOR, (x, y), RADIUS)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()