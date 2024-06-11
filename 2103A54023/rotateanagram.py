'''Rotate a given string in the specified direction by specified magnitude. After each rotaion make a note of the
sample inpt:
carrace
3
L 2
R 2
L 3
output:
no
exp-after applying all rotations the firstcharstring will be "rcr" which is not anagram of any sub string of original string "carrace
rraceac
carrace
racecar"'''
data=input()
qstr=deque(data)
rot=int(input())
res=""
for i in range(rot):
    di,mag=input().split()
    if di =='1' or di == 'L':
        qstr.rotate(-int(mag))
        res+=qstr[0]
    elif di=='r' or di == 'R':
        qstr.rotate(int(mag))
        res+=qstr[0]
subL=[data[i:i+rot] for i in range(0,len(data)-rot+1 )]
for subele in subL:
    if sorted(subele) == sorted(res):
        print("yes")
        break
    else:
        print("no")
