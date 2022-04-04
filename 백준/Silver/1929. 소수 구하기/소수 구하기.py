import math

def prime(n):
    if n ==1:
        False
    else:
        for i in range(2, int(math.sqrt(n) + 1)):
            if n%i==0:
                return False
        return True
    
n, m =map(int, input().split())

for i in range(n, m + 1):
    if prime(i):
        print(i)