import re

a = input()

result = re.findall(r'[A-Z][a-z]*', a)

print(result)