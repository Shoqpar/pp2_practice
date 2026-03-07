import re

a = input()
find = re.findall(r"[A-Z][a-z]+", a)
if find:
    print(*find)
else: print("No")