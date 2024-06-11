t=int(input())
for i in range(t):
    n=int(input())
    numlist=list(map(int,input().split()))
    index=n-1
    for i in range(n-1,0,-1):
        if numlist[i] > numlist[i-1]:
            numlist[i],numlist[i-1]=numlist[i-1], numlist[i]
            index=i
            break
    res=[str(ele) for ele in (numlist[:index]+(numlist[index:])[::-1])]
    print(''.join(res))
    
    
        
    
    