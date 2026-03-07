import re

a = input()
find = re.search(r"a.*b", a)

if find:
    print(find.group())
else: print("No")