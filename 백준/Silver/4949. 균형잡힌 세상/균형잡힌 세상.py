import sys
while True:
    i = sys.stdin.readline().rstrip()
    if i =='.':
        break
    nrr =[]
    for j in i:
        if j=='(' or j=='[':
            nrr.append(j)
        elif j==']':
            if len(nrr)!=0 and nrr[-1] == '[':
                nrr.pop()
            else:
                nrr.append(j)
                break
        elif j==')':
            if len(nrr)!=0 and nrr[-1] == '(':
                nrr.pop()
            else:
                nrr.append(j)
                break
                     
    if len(nrr)==0:
        print('yes')  
    else:
        print('no')   