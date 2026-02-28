import math

print(max(5, 10, 25))    # 25
print(abs(-7.25))        # 7.25
print(round(3.14159, 2)) # 3.14
print(pow(2, 3))         # 8

print(math.sqrt(64))  # 8.0 (Квадратный корень)
print(math.ceil(1.4)) # 2 (Округление вверх)
print(math.floor(1.4))# 1 (Округление вниз)

# Тригонометрия и константы
print(math.sin(math.pi / 2)) # 1.0
print(f"Пи: {math.pi}, Экспонента: {math.e}")

import random

print(random.random())       # Случайное число от 0.0 до 1.0
print(random.randint(1, 10)) # Случайное целое число от 1 до 10 включительно

fruits = ['яблоко', 'банан', 'вишня']
print(random.choice(fruits)) # Случайный элемент из списка

random.shuffle(fruits)       # Перемешивает список на месте
print(fruits)