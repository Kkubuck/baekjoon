import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())

queue = deque(list(i for i in range(1, n+1)))

while True:
    if len(queue)==1:
        break
    queue.popleft()
    queue.append(queue[0])
    queue.popleft()
    
print(queue[0])