import pygame
import sys
import random

pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer with Coins")
clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 223, 0)

# Шрифты для отображения текста
font = pygame.font.SysFont("Verdana", 20)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Замените следующую строку на загрузку картинки: self.image = pygame.image.load("Player.png")
        self.image = pygame.Surface((40, 70))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 100)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if pressed_keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.move_ip(5, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Замените: self.image = pygame.image.load("Enemy.png")
        self.image = pygame.Surface((40, 70))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, 5) # Враг падает вниз
        if self.rect.top > HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH - 40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Монетка. Замените на картинку при желании.
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (10, 10), 10)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), -50)

    def move(self):
        self.rect.move_ip(0, 4) # Монетка движется чуть медленнее врага
        if self.rect.top > HEIGHT:
            self.rect.top = -50
            self.rect.center = (random.randint(40, WIDTH - 40), -50)

# Создание спрайтов
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Группы спрайтов для удобной отрисовки и проверок коллизий
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

score_coins = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    # Движение и отрисовка всех спрайтов
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    # Проверка столкновения с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        # Если врезались, заливаем экран красным и выходим
        screen.fill(RED)
        pygame.display.update()
        pygame.time.delay(1000)
        pygame.quit()
        sys.exit()

    # Проверка сбора монеток
    # Если столкнулись с монеткой, увеличиваем счетчик и возвращаем её наверх
    if pygame.sprite.spritecollideany(P1, coins):
        score_coins += 1
        C1.rect.top = -50 # Респавн монетки сверху
        C1.rect.center = (random.randint(40, WIDTH - 40), -50)

    # Отображение количества собранных монет в правом верхнем углу
    score_text = font.render(f"Coins: {score_coins}", True, WHITE)
    screen.blit(score_text, (WIDTH - 120, 10))

    pygame.display.update()
    clock.tick(60)