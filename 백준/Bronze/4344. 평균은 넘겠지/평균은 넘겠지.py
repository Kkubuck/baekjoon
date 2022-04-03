import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    avg = sum(arr[1:])/arr[0]
    count = 0
    for score in arr[1:]:
        if score > avg:
            count+=1
    result = count/arr[0]*100
    print(f'{result:.3f}%')