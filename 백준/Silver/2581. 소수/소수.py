import sys
m = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
arr = list(i for i in range(m, n+1))

sumarr = []
for i in arr:
    count =0
    for j in range(1, i + 1):
        if i%j==0:
            count+=1
    
    if count==2:
        sumarr.append(i)

if sum(sumarr)>0:       
    print(sum(sumarr))
    print(min(sumarr))
else:
    print(-1)