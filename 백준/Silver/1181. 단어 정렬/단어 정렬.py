arr = []
n = int(input())
for i in range(n):
    arr.append(input())
arr.sort()
arr.sort(key=len)
nrr = []
for i in arr:
    if i not in nrr:
        nrr.append(i)
        print(i)