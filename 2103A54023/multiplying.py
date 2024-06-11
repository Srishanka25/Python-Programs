n1=list(map(int,input().split()))
n2=list(map(int,input().split()))
n1.sort()
n2=sorted(n2)[::-1] #n2=sorted(n2).reverse()
res=0
for i in range(len(n1)):
    res += n1[i] * n2[i]
print(res)