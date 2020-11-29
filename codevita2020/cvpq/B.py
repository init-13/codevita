from math import ceil
for _ in range(int(input())):

    n=int(input())
    x=list(map(int,input().split()))
    z=0
    o=0
    t=0
    for i in x:
        if i%3==0:
            z+=1
        elif i%3==1:
            o+=1
        else:
            t+=1

    if z==0:
        
        if o==n or t==n:
            print('Yes')
        else:
            print('No')
            
    elif z<=ceil(n/2):
        print('Yes')

    else:
        print('No')
