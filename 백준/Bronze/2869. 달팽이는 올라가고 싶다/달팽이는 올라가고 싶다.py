import sys

A, B, V = map(int, sys.stdin.readline().rstrip().split())
day = (V-B)/(A-B)
 
if day == int(day): 
    print(int(day)) 
else:   
    print(int(day + 1))