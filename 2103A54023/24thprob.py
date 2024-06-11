#given tuples inside a list sort based on the second element in each tuple
'''s=int(input())
n=[tuple(map(int,input().split(","))) for i in range(s)]
print(sorted(n,key=lambda x:x[1])) without functions'''
#with functions
def end(data):
    return data[-1]
s=int(input())
n=[tuple(map(int,input().split(","))) for i in range(s)]
res=sorted(n,key=end)
print(res)