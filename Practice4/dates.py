#текущая дата
from datetime import datetime

now = datetime.now()
print(now)

#создание своей даты
from datetime import datetime

my_date = datetime(2025, 6, 10, 15, 30)
print(my_date)

#разница между датами
from datetime import datetime

date1 = datetime(2025, 1, 1)
date2 = datetime(2025, 1, 10)

difference = date2 - date1
print(difference.days)  # 9

#форматирование даты
now = datetime.now()

print(now.strftime("%Y-%m-%d"))
print(now.strftime("%d/%m/%Y"))

import datetime

# Текущая дата и время
now = datetime.datetime.now()
print("Сейчас:", now)

# Создание конкретной даты (Год, Месяц, День)
my_date = datetime.datetime(2023, 5, 17)
print("Моя дата:", my_date)

# Из даты в строку
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Отформатировано:", formatted) # 2026-02-28 09:35:10 (пример)

# Из строки в дату
date_string = "21 June, 2018"
parsed_date = datetime.datetime.strptime(date_string, "%d %B, %Y")
print("Распарсено:", parsed_date)

today = datetime.datetime.now()
new_year = datetime.datetime(today.year + 1, 1, 1)

# Вычисление разницы
time_left = new_year - today
print(f"До Нового года осталось {time_left.days} дней")

# Добавление времени (например, прибавить 10 дней к текущей дате)
ten_days_later = today + datetime.timedelta(days=10)

from zoneinfo import ZoneInfo

# Текущее время в Токио
tokyo_time = datetime.datetime.now(ZoneInfo("Asia/Tokyo"))
print("Время в Токио:", tokyo_time)