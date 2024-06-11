#reverse a string keeping its special character at same place
'''n=input()
l=list(n)
s,e=0,len(l)-1
while s<e:
    if not l[s].isalpha():
        s+=1
    elif not l[e].isalpha():
        e-=1
    else:
        l[s],l[e]=l[e],l[s]
        s+=1
        e-=1
res=''.join(l)
print(res)'''
import re
stri=input()
str_list=re.findall("[a-zA-Z]",stri)
str_list.reverse()
for i in range(len(stri)):
    if(stri[i]=='#' or stri[i]=='@'):
        str_list.insert(i,stri[i])
print(''.join(str_list))
        