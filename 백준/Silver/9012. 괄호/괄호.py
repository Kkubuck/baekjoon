import sys

n = int(sys.stdin.readline().rstrip())
for i in range(n):
    stack = list(sys.stdin.readline().rstrip())
    arr = []
    for i in stack:
        if i=='(':
            arr.append(i)
        if i==')':
            if len(arr)==0:    
                arr.append(i)
                break    
            arr.pop()

    if len(arr)==0:
        print('YES')
    else:
        print('NO')

