'''given a number find its factors and print count of numbers which are not perfect squares excluding 1 and the number itself'''
n=int(input())
l=[]
for i in range(1,n//2+1):
    if n%i==0:
        l.append(i)
squarefree_num=[]
for j in l:
    r=j**0.5
    if r!=int(r):
        squarefree_num.append(j)
print(squarefree_num)
print(len(squarefree_num))
