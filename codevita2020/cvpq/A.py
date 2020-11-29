input()
m=0
ml=list()
x='A'+input()+'B'
va=0
vb=0
for i in x:
    if i=='-':
        m+=1
    else:
        
        if m:
            ml.append(m)
        m=0

        if i=='A':
            va+=1
        else:
            vb+=1
            
xl=list(x.split('-'))

#print(xl)
ss=''
for i in xl:
    if i:
        ss+=i
        if ml:
            ss+=str(ml.pop(0))
for i in range(len(ss)):
    if ss[i].isdigit() and ss[i-1]==ss[i+1]:
        if ss[i-1]=='A':
            va+=int(ss[i])
        else:
            vb+=int(ss[i])
            
if va>vb:
    print('A')
elif vb>va:
    print('B')
else:
    print('Coalition government')
        
        











        
