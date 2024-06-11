#checking a number whether it is a power of 6 or not
num=int(input()) 
while num!=1:
    if num%6==0:
        num//6
    else:
        print("false")
        break
else:
    print("true")