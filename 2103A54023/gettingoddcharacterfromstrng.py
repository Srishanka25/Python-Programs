data="Hello Everyone"
relist=[]
for i in range(len(data)):
    if i%2!=0:
        relist.append(data[i])
ores=[]
for ch in data[1::2]:
    ores.append(ch)
print(relist)
print(ores)

print([data[i] for i in range(len(data)) if i%2!=0])
print([ch for ch in data[1::2]])
