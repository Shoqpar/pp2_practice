import json
#Перевод строки формата JSON в словарь Python

# JSON строка (обрати внимание на использование двойных кавычек внутри!)
x = '{"name": "Ivan", "age": 30, "city": "Almaty"}'

# Парсинг: из JSON-строки в Python словарь
y = json.loads(x)
print(y["age"]) # Выведет 30

#Конвертация Python в JSON

user = {
  "name": "Anna",
  "age": 25,
  "is_student": True,
  "hobbies": ["reading", "cycling"]
}

# Из Python в JSON-строку
# indent=4 делает вывод красивым (с отступами)
user_json = json.dumps(user, indent=4)
print(user_json)