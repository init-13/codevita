def roots(a,b,c):
    D=b**2 - 4*a*c
    ro=(D**0.5 - b)/2
    return ro

x1=int(input())
x2=int(input())
y1=int(input())
y2=int(input())
v=float(input())

a=(v*x1)**2 - x2**2
b=2*(x2**2*x1 - v*x1**2*x2)
c=(v*x1*y2)**2 - (x2*y1)**2

print(roots(a,b,c))
