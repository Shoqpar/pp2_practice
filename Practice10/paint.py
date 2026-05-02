import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Extended Paint")
font = pygame.font.SysFont("Verdana", 16)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BG_COLOR = WHITE

# Базовый слой хранит готовые фигуры, чтобы они не стирались при анимации новой фигуры
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill(BG_COLOR)

current_color = BLACK
brush_size = 5
tool = "brush" # Доступные инструменты: brush, rect, circle, eraser

drawing = False
start_pos = (0, 0)
current_pos = (0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Нажатие мыши (начало рисования)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            drawing = True
            start_pos = event.pos
            current_pos = event.pos

        # Движение мыши
        if event.type == pygame.MOUSEMOTION:
            if drawing:
                current_pos = event.pos
                # Кисть и ластик рисуют непрерывно сразу на base_layer
                if tool == "brush":
                    pygame.draw.line(base_layer, current_color, start_pos, current_pos, brush_size)
                    start_pos = current_pos # Обновляем позицию для плавности
                elif tool == "eraser":
                    # Ластик - это та же кисть, но цвета фона (белый) с увеличенным размером
                    pygame.draw.line(base_layer, BG_COLOR, start_pos, current_pos, brush_size + 15)
                    start_pos = current_pos

        # Отпускание мыши (финализация фигур)
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            drawing = False
            current_pos = event.pos
            
            # Прямоугольник и круг рисуются один раз при отпускании
            if tool == "rect":
                # Создаем корректный прямоугольник вне зависимости от того, куда тянули мышь
                rect = pygame.Rect(min(start_pos[0], current_pos[0]), min(start_pos[1], current_pos[1]),
                                   abs(current_pos[0] - start_pos[0]), abs(current_pos[1] - start_pos[1]))
                pygame.draw.rect(base_layer, current_color, rect, brush_size)
            
            elif tool == "circle":
                # Вычисляем радиус по теореме Пифагора (расстояние от центра до края)
                dx = current_pos[0] - start_pos[0]
                dy = current_pos[1] - start_pos[1]
                radius = int(math.hypot(dx, dy))
                pygame.draw.circle(base_layer, current_color, start_pos, radius, brush_size)

        # Обработка клавиатуры (выбор инструментов и цвета)
        if event.type == pygame.KEYDOWN:
            # Выбор инструмента
            if event.key == pygame.K_1: tool = "brush"
            elif event.key == pygame.K_2: tool = "rect"
            elif event.key == pygame.K_3: tool = "circle"
            elif event.key == pygame.K_e: tool = "eraser"
            
            # Выбор цвета
            elif event.key == pygame.K_r: current_color = RED
            elif event.key == pygame.K_g: current_color = GREEN
            elif event.key == pygame.K_b: current_color = BLUE
            elif event.key == pygame.K_k: current_color = BLACK
            
            # Очистка
            elif event.key == pygame.K_c:
                base_layer.fill(BG_COLOR)

    # Отрисовка
    screen.fill(BG_COLOR)
    screen.blit(base_layer, (0, 0)) # Сначала рисуем готовый фон

    # Если рисуем фигуру, показываем её "превью" поверх фона (чтобы было видно размер)
    if drawing:
        if tool == "rect":
            preview_rect = pygame.Rect(min(start_pos[0], current_pos[0]), min(start_pos[1], current_pos[1]),
                                       abs(current_pos[0] - start_pos[0]), abs(current_pos[1] - start_pos[1]))
            pygame.draw.rect(screen, current_color, preview_rect, brush_size)
        elif tool == "circle":
            radius = int(math.hypot(current_pos[0] - start_pos[0], current_pos[1] - start_pos[1]))
            pygame.draw.circle(screen, current_color, start_pos, radius, brush_size)

    # Панель подсказок
    panel_text = font.render(f"Tool: {tool.upper()} (1=Brush, 2=Rect, 3=Circle, E=Eraser) | Colors: R, G, B, K(Black) | C=Clear", True, BLACK)
    pygame.draw.rect(screen, (220, 220, 220), (0, 0, WIDTH, 30))
    screen.blit(panel_text, (10, 5))

    pygame.display.flip()

pygame.quit()