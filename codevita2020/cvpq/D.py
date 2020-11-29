
def cv(s):
    c=0
    for i in s:
        if i in 'aeiou':
            c+=1
    return c

def n2w(n):

    s= ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
  
    
    d= ["ten", "eleven", "twelve","thirteen", "fourteen", "fifteen","sixteen", "seventeen", "eighteen","nineteen"]
  
     
    ten= ["twenty", "thirty", "forty","fifty", "sixty", "seventy", "eighty","ninety"]
    
    if n==100:
        return 'hundred'
    if n>9:
        if n<20:
            return (d[n%10])
        else:
            sm=(ten[n//10 - 2])
            if n%10:
                sm+=' '+s[n%10]
            return sm
                
    return (s[n%10])


def nop(s,n):
    xs=set()

    sl=len(s)
    x=0
    for i in range(sl):
        for j in range(sl):
            if i!=j and s[i]+s[j]==n:
                if (s[i] not in xs) or (s[j] not in xs):
                    #print(s[i],s[j])
                    x+=1
                    xs.add(s[i])
                    xs.add(s[j])

    #x=len(xs)
    #print(xs,x)
    if x>100:
        print('greater 100')
    else:
        print(n2w(x))


#(nop([4,4,5,3,6,7,2],9))
#for i in range(101):
    #print(n2w(i),cv(n2w(i)))
    
input()
x=list(map(int,input().split()))
s=0
for i in x:
    s+=cv(n2w(i))

#print(s)
nop(x,s)


    
