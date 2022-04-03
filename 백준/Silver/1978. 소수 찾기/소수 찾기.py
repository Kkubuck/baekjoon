import sys

num = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
all = 0
for i in arr:
    count =0
    for j in range(1, i + 1):
        if i%j==0:
            count+=1
    
    if count==2:
        all+=1
print(all)