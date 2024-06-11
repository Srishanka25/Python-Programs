a=list(map(int,input().split()))
print(a)
a[0],a[-1]=a[-1],a[0]
print(a)