import sys

string = list(sys.stdin.readline().rstrip().upper())
ardic = dict()

for i in range(len(string)):
    ardic[string[i]] =0
for i in range(len(string)):
    ardic[string[i]] +=1

max = 0

for key, value in ardic.items():
    if max == value:
        maxs = '?'
    if max < value:
        max = value
        maxs = key
print(maxs)