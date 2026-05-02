import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Practice 11 - Racer")
clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
RED = (220, 40, 40)
BLUE = (40, 90, 220)
YELLOW = (240, 210, 50)
GREEN = (50, 200, 80)

font = pygame.font.SysFont("Verdana", 20)
big_font = pygame.font.SysFont("Verdana", 48)

# Main game variables
score = 0
coins_collected = 0
enemy_speed = 5
N = 5  # enemy speed increases after every N coins


class Player(pygame.sprite.Sprite):
    """Player car controlled by left and right arrow keys."""
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((45, 80))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 70))
        self.speed = 6

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Do not allow the player to leave the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH


class Enemy(pygame.sprite.Sprite):
    """Enemy car that falls from the top."""
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((45, 80))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-300, -80)

    def update(self):
        global score
        self.rect.y += enemy_speed

        # If enemy goes below screen, reset it and add score
        if self.rect.top > HEIGHT:
            score += 1
            self.reset_position()


class Coin(pygame.sprite.Sprite):
    """Coin with random weight. Bigger weight gives more points."""
    def __init__(self):
        super().__init__()
        self.weight = random.choice([1, 2, 3])
        self.radius = 10 + self.weight * 3
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)

        # Draw coin circle
        pygame.draw.circle(self.image, YELLOW, (self.radius, self.radius), self.radius)
        pygame.draw.circle(self.image, BLACK, (self.radius, self.radius), self.radius, 2)

        self.rect = self.image.get_rect()
        self.reset_position()
        self.speed = 4

    def reset_position(self):
        self.weight = random.choice([1, 2, 3])
        self.radius = 10 + self.weight * 3
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (self.radius, self.radius), self.radius)
        pygame.draw.circle(self.image, BLACK, (self.radius, self.radius), self.radius, 2)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-500, -50)

    def update(self):
        self.rect.y += self.speed

        # If coin was missed, generate a new one
        if self.rect.top > HEIGHT:
            self.reset_position()


player = Player()
enemy = Enemy()
coins = pygame.sprite.Group()

# Gеnerate several coins on the road
for _ in range(4):
    coins.add(Coin())

all_sprites = pygame.sprite.Group(player, enemy, *coins)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    # Check coin collision
    collected_coins = pygame.sprite.spritecollide(player, coins, False)
    for coin in collected_coins:
        coins_collected += coin.weight
        score += coin.weight
        coin.reset_position()

        # Increase enemy speed when player earns N coins
        if coins_collected % N == 0:
            enemy_speed += 1

    # Check enemy collision
    if pygame.sprite.collide_rect(player, enemy):
        screen.fill(RED)
        text = big_font.render("Game Over", True, BLACK)
        screen.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False

    # Draw road
    screen.fill(GRAY)
    pygame.draw.line(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 4)

    all_sprites.draw(screen)

    info = font.render(f"Score: {score}  Coins: {coins_collected}  Speed: {enemy_speed}", True, WHITE)
    screen.blit(info, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
