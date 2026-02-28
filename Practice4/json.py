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

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None)) 

#Чтение и запись

# Открываем файл для чтения ('r')
with open('sample-data.json', 'r', encoding='utf-8') as file:
    data = json.load(file) # Теперь data - это словарь или список Python
    
    # Работаем с данными
    print("Данные загружены успешно!")

# Изменяем наши данные (например, добавляем новое поле)
data["last_updated"] = "2026-02-28"

# Записываем обновленные данные обратно в файл ('w' - write)
with open('sample-data-updated.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)


