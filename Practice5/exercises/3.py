import re

a = input()
find = re.findall(r"[a-z]+_[a-z]+", a)
if find:
    print(*find)
else: print("No")