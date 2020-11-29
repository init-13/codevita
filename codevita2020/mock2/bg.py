
def main():
    nl=int(input())

    b=input()
    gc=input()

    r=gc.count('r')
    m=gc.count('m')

    

    for i in range(nl):
        
        if b[i]=='r':
            if not r:
                return nl-i

            else: r-=1

        elif b[i]=='m':
            if not m:
                return nl-i

            else: m-=1

    return 0


print(main())
            
