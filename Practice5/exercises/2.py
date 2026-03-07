import re

a = input()
result = re.search(r"ab{2,3}", a)
if result:
    print(result.group())
else: print("No")