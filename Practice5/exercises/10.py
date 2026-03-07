import re

a = input()

result = re.sub(r'(?<!^)([A-Z])', lambda m: "_" + m.group(1), a).lower()

print(result)