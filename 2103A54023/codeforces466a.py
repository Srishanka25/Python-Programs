l=list(map(int,input().split()))
r=l[0]*l[2]

d=l[0]//l[1]
e=d*l[3]
f=l[0]%l[1]
g=f*l[2]
s=e+g
print(min(r,s))
#2
n,m,a,b=list(map(int,input().split()))
if m*a <=b:
    print(n*a)
else:
    print((n//m)*b+min((n%m)*a,b))