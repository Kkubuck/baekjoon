import sys

def pibonachi(n):
    if n <= 1:
        return n
    return pibonachi(n-1) + pibonachi(n-2)
    
a = int(sys.stdin.readline().rstrip())
print(pibonachi(a))