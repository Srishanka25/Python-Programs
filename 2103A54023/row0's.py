'''#mani is given an n-by-n matrix of 0's and 1's where all 1's in each row come before all 0's his task is to find the most efficient way to return
the row with the max no.of 0's'''
({1,1,1,1},{1,1,0,0},{1,0,0,0},{1,1,0,0})
'''for i in range(int(input())):
    nestList=list(map(int,input().split()))
    n=len(nestList)
    nestList=[nestList]
    for i in range(n-1):
        nestList.append(list(map(int,input().split())))
mcount=0
for i in range(n):
    if mcount < nestList[i].count(0):
        mcount=nestList[i].count(0)
        index=i
print(mcount)'''
t=int(input())
f=[]
for i in range(t):
    l=list(map(int,input().split()))
    f.append(l)
    for j in range(len(l)-1):
        k=list(map(int,input().split()))  
        f.append(k)
c=0
for i in range(len(f)):
    if c < f[i].count(0):
        c=f[i].count(0)
        c=i
print(c)