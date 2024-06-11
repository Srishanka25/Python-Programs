#codeforces 427A police question
n=int(input())
l=list(map(int,input().split()))
avapolice=0
unevents=0
for eve in l:
    if eve > 0:
        avapolice+=eve
    elif eve==-1:
        if avapolice <= abs(eve):
            unevents+=abs(eve)-avapolice
            avapolice=0
        else:
            avapolice-=abs(eve)
print(unevents)
            
        