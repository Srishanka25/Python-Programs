'''array manipulation
input
1
4
1234
output-19
input
1
5
12345
output=34'''
for i in range(int(input())):
    N=int(input())
    containers=list(map(int,input().split()))
    totsum=containers[0]
    totTime=0
    for i in containers[1:]:
        totsum+=i
        totTime+=totsum
    print(totTime)
