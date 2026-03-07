import re

a = input()
match = re.compile(r"\s|,|\.")
print(match.sub(":", a))