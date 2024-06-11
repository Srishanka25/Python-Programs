n=int(input())
nestlist=[list(map(int,input().split())) for i in range(n)]
maxin,tsum = 0,0
for index,data in enumerate(nestlist):
    if tsum <sum(data):
        tsum = sum(data)
        maxin=index
print(maxin)