'''n = int(input())
p = list(map(int, input().split()))
result = [0] * n
for i in range(n):
    result[p[i] - 1] = i + 1
print(" ".join(map(str, result)))'''

n=int(input())
flist=list(map(int,input().split()))
info={}
k=1
for i in flist:
    info[i-1]=k
    k+=1
for i in range(n):
    print(info[i],end=' ')