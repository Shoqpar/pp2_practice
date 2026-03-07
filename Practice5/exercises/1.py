import re

a = input()
result = re.search(r"ab*", a)
if result:
    print(result.group())
else: print("No")