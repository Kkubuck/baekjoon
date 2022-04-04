import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())

queue =deque([])

for i in range(n):
    ans = sys.stdin.readline().rstrip().split()

    if ans[0]=='push':
        queue.append(ans[1])
    
    if ans[0]=='pop':
        if len(queue):
            print(queue.popleft())
        else:
            print(-1)

    if ans[0]=='size':
        print(len(queue))
    
    if ans[0]=='empty':
        if len(queue):
            print(0)
        else:
            print(1)
    
    if ans[0]=='front':
        if len(queue):
            print(queue[0])
        else:
            print(-1)

    if ans[0]=='back':
        if len(queue):
            print(queue[-1])
        else:
            print(-1)
    
