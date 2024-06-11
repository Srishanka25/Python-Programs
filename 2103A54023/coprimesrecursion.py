def coprimes(n,m):
    while m != 0:
        n, m = m, n % m
    if n==1:
        return "co-prime"
    else:
        return"not a co-prime"
     
n,m=map(int,input().split())
print(coprimes(n,m))