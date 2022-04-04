from audioop import minmax
import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

if a>b:
    maxi = a
    mini = b
else:
    maxi = b
    mini = a
for i in range(1, maxi + 1):
    if a%i==0 and b%i==0:
        maxm = i
print(maxm)
i = 1
while True:
    if (i*mini)%maxi ==0:
        print(i*mini)
        break
    i+=1