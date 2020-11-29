def ifp(s):
    for i in range(len(s)//2):
        if s[i]!=s[-(i+1)]:
            return False
    return True

#print(ifp('nayan'))



x=list()
y=list()
s=input()+'#'
#ml=list()
c1=s[0]
for i in range(len(s)):
    if s[i]==c1:
        x.append(i+1)

#print(x)
for i in x:
    c2=s[i]
    #print(c2)
    for j in range(i,len(s)-1):
        #print(c2,s[j],s[j+1],s[-2])
        if s[j]==c2 and s[j+1]==s[-2]:
            y.append([i,j+1])
for i in y:
    a=i[0]
    b=i[1]
    if(ifp(s[:a]) and ifp(s[a:b]) and ifp(s[b:-1])):
        print(s[:a])
        print(s[a:b])
        print(s[b:-1])
        break
        
