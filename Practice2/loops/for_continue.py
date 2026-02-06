for x in range (6):
    if x == 3:
        continue
    print (x)

n = int(input())

for i in range (1, n+1):
    if i % 3 == 0:
        continue
    print(i)