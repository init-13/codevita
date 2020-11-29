

nl=int(input())

xl=list(map(int,input().split()))

op=dict()
ep=dict()
#print(xl)
for x in range(nl):
    #print(x)
    t=str(xl[x])
    if x%2:
        n=int(str(11*int(max(t))+7*int(min(t)))[-2:])
        #print(int(max(t)),int(min(t)),n)
        n1=int(str(n)[0])
        if n1 in op:
            op[n1].append(n)
        else:
            op[n1]=[n]
    else:
        n=int(str(11*int(max(t))+7*int(min(t)))[-2:])
        
        #print(int(max(t)),int(min(t)),n)
        n1=int(str(n)[0])
        if n1 in ep:
            ep[n1].append(n)
        else:
            ep[n1]=[n]
        
s=0
#print(op,ep)
for x in op:
    if len(op[x])>1  :

        if len(set(op[x]))==1:
            s+= 1
        else :
            s+=2

for x in ep:
    if len(ep[x])>1  :

        if len(set(ep[x]))==1:
            s+= 1
        else :
            s+=2


print(s)

        

    
