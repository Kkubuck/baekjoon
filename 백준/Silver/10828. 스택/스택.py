import sys
stack =[]
n = int(input())

for i in range(n):

    ans = sys.stdin.readline().rstrip().split()

    if ans[0] =='push':
        stack.append(int(ans[1]))

    if ans[0] =='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())

    if ans[0] =='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)

    if ans[0] =='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])

    if ans[0] =='size':
        print(len(stack))