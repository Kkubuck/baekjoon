arr = set(range(1, 10001))
num = set()

for i in range(1, 10001):
    for j in str(i):
        i+=int(j)
    num.add(i)

all = sorted(arr - num)

for i in all:
    print(i, end= ' ')