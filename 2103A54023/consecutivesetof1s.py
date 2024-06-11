'''nums=list(map(int,input().split(",")))
c=0
res=[]
for i in range(2,len(nums)):
    if nums[i-1]==nums[i]:
        c+=1
    res.append(c)
print(max(res))'''

'''n=list(map(int,input().split(",")))
c,d=0,0
for i in range(len(n)):
    if n[i]==1:
        c+=1
        if c>d:
            d=c
    else:
        c=0
print(d)''' 

        