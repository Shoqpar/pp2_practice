import re
import json
from pathlib import Path

file_path = Path(__file__).parent / "raw.txt"

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1

price_pattern = re.compile(r"\d[\d ]*,\d{2}")
prices = price_pattern.findall(text)


# 2

product_pattern = re.compile(r"\n\d+\.\n(.+)")
products = product_pattern.findall(text)



# 3

total_pattern = re.search(r"ИТОГО:\s*\n([\d ]+,\d{2})", text)

if total_pattern:
    total = total_pattern.group(1)
else:
    total = None



# 4

datetime_pattern = re.search(r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s*(\d{2}:\d{2}:\d{2})", text)

if datetime_pattern:
    date = datetime_pattern.group(1)
    time = datetime_pattern.group(2)
else:
    date = None
    time = None


# 5

payment_pattern = re.search(r"(Банковская карта|Наличные)", text)

if payment_pattern:
    payment_method = payment_pattern.group(1)
else:
    payment_method = None


# 6

result = {
    "products": products,
    "prices": prices,
    "total": total,
    "date": date,
    "time": time,
    "payment_method": payment_method
}


print(json.dumps(result, indent=4, ensure_ascii=False))