tcase=int(input())
for t in range(tcase):
    n,k=list(map(int,input().split()))
    array=list(map(int,input().split()))
    print(k-min(array))
    
    