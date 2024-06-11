'''Question:- There are n houses build in a line, each of which contains some value in it.A thief is going to steal the maximal value of these houses, but he can’t steal in two adjacent houses because the owner of the stolen houses will tell his two neighbours left and right side.
What is the maximum stolen value?Sample Input: val[] = {6, 7, 1, 3, 8, 2, 5}Sample Output: 20'''
 
'''num = list(map(int,input().split(",")))
even, odd = 0, 0
for i in range(0,len(num), 2):
    odd+=num[i]
for i in range(1,len(num), 2):
    even+=num[i]
print(max(even,odd))'''

house=list(map(int,input().split()))
emax=sum(house[0::2])
omax=sum(house[1::2])
tmax=0
while(max(house)!=0):
    tmax+=max(house)
    i=house.index(max(house))
    if i==0:
        house[0],house[1]=0,0
    elif i== len(house)-1:
        house[-2],house[-1]=0,0
    else:
        house[i],house[i+1],house[i-1] = 0,0,0
print(max([omax,emax,tmax]))

            
