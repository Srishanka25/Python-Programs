nl=list(input().split())
for i in range(len(nl)):
    if i % 2==0:
        if '.' not in str(nl[i]):
            print("False")
            break
    else:
       # if nl[i].is_integer() == 'int':
       if '.' not in str(nl[i]):
           print('False')
           break
   else:
    print('True') 