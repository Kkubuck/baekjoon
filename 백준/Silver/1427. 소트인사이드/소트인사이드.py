arr = list(map(int, input()))
narr = sorted(arr, reverse=True)
for i in narr:
    print(i, end='')