n,t=map(int,input().split())
s=list(input())
for _ in range(t):
    i=1
    while i < len(s):
        if s[i]=='G' and s[i-1]=='B':
            s[i]='B'
            s[i-1]='G'
            i+=1
        i+=1
print(''.join(s))