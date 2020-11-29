def ipr(s,status):
    if '/' not in s:
        x=s
        n=32
    else:
        x,n=s.split('/')

    ipl=list(map(int,x.split('.')))
    if status:
        n=32
        ipl.pop()
        ipl.append(255)
    c=''
    for i in ipl:
        c+=('0'*7+bin(i)[2:])[-8:]
    ss=''
    for i in range(len(c)):
        if i<int(n):
            ss+=c[i]
        else:
            ss+='0'
    #print(ss)
    return int(ss,2)


#ipr('7.25.255.0')
#ipr('7.25.255.0/20')

r,n=map(int,input().split())
x=list()
for i in range(r):
    l,h,reg=input().split()
    
    x.append((ipr(l,0),ipr(h,1),reg))
x.append('None')

#print(x)

for _ in range(n):

    xp=ipr(input(),0)
    #print(xp)

    for i in range(r+1):
        try:
            if xp>=x[i][0] and xp<=x[i][1]:
                print(x[i][2])
                break
        except:
            print('None')
            #print(i)
            break
            
            
        
        
