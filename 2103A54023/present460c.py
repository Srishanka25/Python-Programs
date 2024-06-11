n,m,w=map(int,input().split())
flower=list(map(int,input().split()))
minH=min(flower)
print(minH+abs(m-w))
    