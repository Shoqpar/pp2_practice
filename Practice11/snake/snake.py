import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
BLOCK = 20
FPS = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Practice 11 - Snake")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", 20)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (40, 200, 80)
RED = (230, 50, 50)
YELLOW = (240, 220, 50)
BLUE = (50, 120, 230)


class Food:
    """Food has random position, random weight, and disappears after timer."""
    def __init__(self):
        self.spawn()

    def spawn(self):
        self.x = random.randrange(0, WIDTH, BLOCK)
        self.y = random.randrange(0, HEIGHT, BLOCK)
        self.weight = random.choice([1, 2, 3])
        self.spawn_time = pygame.time.get_ticks()
        self.life_time = random.randint(4000, 7000)  # миллисекунды

    def is_expired(self):
        current_time = pygame.time.get_ticks()
        return current_time - self.spawn_time > self.life_time

    def draw(self):
        # еда разного объема имеют разные цвета
        color = RED
        if self.weight == 2:
            color = YELLOW
        elif self.weight == 3:
            color = BLUE

        pygame.draw.rect(screen, color, (self.x, self.y, BLOCK, BLOCK))


snake = [(WIDTH // 2, HEIGHT // 2)]
direction = "RIGHT"
next_direction = "RIGHT"
score = 0
food = Food()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # изменение положения
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                next_direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                next_direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                next_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                next_direction = "RIGHT"

    direction = next_direction
    head_x, head_y = snake[0]

    direction = next_direction
    head_x, head_y = snake[0]

    # 1. Движение головы
    if direction == "UP":
        head_y -= BLOCK
    elif direction == "DOWN":
        head_y += BLOCK
    elif direction == "LEFT":
        head_x -= BLOCK
    elif direction == "RIGHT":
        head_x += BLOCK

    # 2. Закольцовка (проход сквозь стены)
    if head_x >= WIDTH: head_x = 0
    elif head_x < 0: head_x = WIDTH - BLOCK
    elif head_y >= HEIGHT: head_y = 0
    elif head_y < 0: head_y = HEIGHT - BLOCK

    new_head = (head_x, head_y)

    # 3. Проверка на столкновение с собой
    if new_head in snake:
        running = False
    
    # 4. Добавляем новую голову
    snake.insert(0, new_head)

    # 5. Еда и хвост
    if head_x == food.x and head_y == food.y:
        score += food.weight
        for _ in range(food.weight - 1):
            snake.append(snake[-1])
        food.spawn()
    else:
        snake.pop()

    # еда исчезает через некоторое время
    if food.is_expired():
        food.spawn()

    screen.fill(BLACK)

    food.draw()

    # вывод змеи
    for part in snake:
        pygame.draw.rect(screen, GREEN, (part[0], part[1], BLOCK, BLOCK))

    text = font.render(f"Score: {score}  Food weight: {food.weight}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
