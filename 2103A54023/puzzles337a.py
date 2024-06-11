n,m=map(int,input().split())
f=list(map(int,input().split()))
minR=abs(min(f[:n])-max(f[:n]))
for i in range(1,m-n):
    minR=min(minR,abs(min(f[:n])-max(f[:n])))
print(minR)