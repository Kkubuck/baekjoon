import sys

n = int(sys.stdin.readline().rstrip())
arr = [[0 for _ in range(2)] for _ in range(20)]
for i in range(n):
    arr = list(sys.stdin.readline().rstrip().split())
    ans = int(arr[0])
    for j in arr[1]:
        print(j * ans, end ='')
    print()