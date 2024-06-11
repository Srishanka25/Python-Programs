#haiku #78
data1=input()
data2=input()
data3=input()
vowels=['a','e','i','o','u']
haiku=[5,7,5]
res=[]
for i in (data1,data2,data3):
    count=0
    for c in i:
        if c in vowels:
            count+=1
    res.append(count)
if res==haiku:
    print("yes")
else:
    print("no")
            