import re

a = input()

result = re.sub(r'_([a-z])', lambda m: m.group(1).upper(), a)

print(result)