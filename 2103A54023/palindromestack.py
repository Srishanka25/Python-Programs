#palindrome using stacks
strData=input()
stack=list(strData)
print(stack)
for i in strData:
    if stack.pop!=i:
        print("Not a palindrome")
        break
else:
    print("palindrome")