import sys

n = int(sys.stdin.readline().rstrip())

for z in range(n):
    arr = list(sys.stdin.readline().rstrip())
    count = 1
    sum=0
    for i in range(len(arr)):
        if arr[i] == 'O':
            sum+=count
            count +=1
        if arr[i] == 'X':
            count = 1
        i+=1
    print(sum)