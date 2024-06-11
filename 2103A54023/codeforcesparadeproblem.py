n=int(input())
trucks=list(map(int,input().split()))
side=[]
result=[]
for i in range(0,len(trucks)-1):
    if trucks[i]>trucks[i+1]:
        side.append(trucks[i])
    else:
        