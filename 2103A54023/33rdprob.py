#program to print sum of all odd numbers present in alrge number
n=int(input())
s=str(n)
l=list(s)
print(l)
summ=0
for i in l:
    if int(i)%2!=0:
        summ+=int(i)
print(summ)
'''other approach
while num!=0:
r=num%10
r%2!=0:
s+=r
can also use a list of odd numbers'''