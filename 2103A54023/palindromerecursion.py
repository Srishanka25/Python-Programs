def palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])
input_p = input()
result = palindrome(input_p)
if result:
    print("True")
else:
    print( "False")
    
'''def palindrome(n):
    original=n
    res=0
    while n>0:
        r=n%10
        res=(res*10)+r
        n=n//10
    if original==res:
        return "True"
    else:
        return "False"
    
n=int(input())
print(palindrome(n))'''

# generating palindrome from the string
data=input()
def largestpal():
    maxlen=0
    larpal=''
    for i in range(len(data)):
        for j in range(i+1,len(data)+1):
            substr=data[i:j]
            if palindrome(substr):
                if len(substr) > maxlen:
                    maxlen=len(substr)
                    larpal=substr
    return larpal
print(largestpal())
        
    
