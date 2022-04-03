import sys

a, b = sys.stdin.readline().rstrip().split()

arr=[]
arr.append(int(a[::-1]))
arr.append(int(b[::-1]))

print(max(arr))