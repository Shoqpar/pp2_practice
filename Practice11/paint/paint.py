import pygame
import math

# Инициализация пайгейм
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Practice 11 - Paint")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", 16)

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 50, 50)
BLUE = (50, 100, 220)
GREEN = (50, 180, 90)
PURPLE = (150, 60, 200)

# base_layer это поверхность, где сохраняются уже нарисованные фигуры
# Экран отображает base_layer + временную фигуру при рисовании
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill(WHITE)
screen.blit(base_layer, (0, 0))

# Переменные состояния инструмента
color = BLACK
thickness = 3
tool = "square"
drawing = False
start_pos = (0, 0) # Точка нажатия мыши
current_pos = (0, 0) # Текущее положение курсора


def get_rect_from_points(p1, p2):
    """Создает корректный прямоугольник (Rect) по двум точкам независимо от направления движения мыши."""
    x1, y1 = p1
    x2, y2 = p2
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))


def draw_square(surface, p1, p2):
    """Рисует квадрат, используя минимальную сторону из области выделения."""
    x1, y1 = p1
    x2, y2 = p2
    side = min(abs(x2 - x1), abs(y2 - y1))
    x = x1 if x2 >= x1 else x1 - side
    y = y1 if y2 >= y1 else y1 - side
    pygame.draw.rect(surface, color, (x, y, side, side), thickness)


def draw_right_triangle(surface, p1, p2):
    """Рисует прямоугольный треугольник внутри выделенной области."""
    rect = get_rect_from_points(p1, p2)
    # Точки: верхний левый угол, нижний левый и нижний правый
    points = [rect.topleft, rect.bottomleft, rect.bottomright]
    pygame.draw.polygon(surface, color, points, thickness)


def draw_equilateral_triangle(surface, p1, p2):
    """Рисует равносторонний треугольник."""
    x1, y1 = p1
    x2, y2 = p2
    side = abs(x2 - x1)
    height = int(side * math.sqrt(3) / 2) # Расчет высоты через корень из 3

    # Корректировка направления отрисовки в зависимости от движения мыши
    if x2 < x1:
        side = -side
    if y2 < y1:
        height = -height

    points = [
        (x1, y1),
        (x1 + side, y1),
        (x1 + side // 2, y1 + height)
    ]
    pygame.draw.polygon(surface, color, points, thickness)


def draw_rhombus(surface, p1, p2):
    """Рисует ромб, вписанный в выделенный прямоугольник."""
    rect = get_rect_from_points(p1, p2)
    points = [
        (rect.centerx, rect.top),    # Верхняя точка
        (rect.right, rect.centery),  # Правая точка
        (rect.centerx, rect.bottom), # Нижняя точка
        (rect.left, rect.centery)    # Левая точка
    ]
    pygame.draw.polygon(surface, color, points, thickness)


def draw_selected_shape(surface, p1, p2):
    """Вызывает функцию рисования в зависимости от выбранного инструмента."""
    if tool == "square":
        draw_square(surface, p1, p2)
    elif tool == "right_triangle":
        draw_right_triangle(surface, p1, p2)
    elif tool == "equilateral_triangle":
        draw_equilateral_triangle(surface, p1, p2)
    elif tool == "rhombus":
        draw_rhombus(surface, p1, p2)


# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обработка нажатия мыши (начало рисования)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            drawing = True
            start_pos = event.pos

        # Обработка движения мыши (превью фигуры)
        if event.type == pygame.MOUSEMOTION and drawing:
            current_pos = event.pos
            # Сначала рисуем старые объекты (base_layer), потом временную фигуру поверх
            screen.blit(base_layer, (0, 0))
            draw_selected_shape(screen, start_pos, current_pos)

        # Обработка отпускания мыши (сохранение фигуры)
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            drawing = False
            current_pos = event.pos
            # Финальная отрисовка и перенос результата в base_layer
            screen.blit(base_layer, (0, 0))
            draw_selected_shape(screen, start_pos, current_pos)
            base_layer.blit(screen, (0, 0))

        # Управление с клавиатуры
        if event.type == pygame.KEYDOWN:
            # Выбор инструмента
            if event.key == pygame.K_1: tool = "square"
            elif event.key == pygame.K_2: tool = "right_triangle"
            elif event.key == pygame.K_3: tool = "equilateral_triangle"
            elif event.key == pygame.K_4: tool = "rhombus"

            # Выбор цвета
            elif event.key == pygame.K_r: color = RED
            elif event.key == pygame.K_g: color = GREEN
            elif event.key == pygame.K_b: color = BLUE
            elif event.key == pygame.K_k: color = BLACK
            elif event.key == pygame.K_p: color = PURPLE

            # Изменение толщины линий
            elif event.key == pygame.K_EQUALS: thickness += 1
            elif event.key == pygame.K_MINUS: thickness = max(1, thickness - 1)

            # Очистка экрана
            elif event.key == pygame.K_c:
                base_layer.fill(WHITE)
                screen.blit(base_layer, (0, 0))

    # Отображение панeели инструментов вверху экрана
    if not drawing:
        screen.blit(base_layer, (0, 0))

    panel = font.render(
        "1 Square | 2 Right Triangle | 3 Equilateral Triangle | 4 Rhombus | R/G/B/K/P colors | +/- size | C clear",
        True,
        BLACK
    )
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, 28)) # Фон панели
    screen.blit(panel, (10, 5)) # Текст панели

    pygame.display.flip()
    clock.tick(60)

pygame.quit()