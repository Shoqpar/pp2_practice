import re

a = input()
result = re.sub(r"(?<!^)([A-Z])", r" \1", a)
print(result)