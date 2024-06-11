#leetcode2390
def removeStars(s):
    stack = []
    for char in s:
        if char == '*':
            if stack:
                stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)


s1 = input()
s2 = input()
print(removeStars(s1)) 
print(removeStars(s2))  
