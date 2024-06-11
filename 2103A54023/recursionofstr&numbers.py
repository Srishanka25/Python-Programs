'''def print_r(n):#printing 5 to 1 recurively
    if n < 1:
        return
    print(n,end=" ")
    print_r(n - 1)
    
print_r(5)'''


'''def print_n(n):
    if n > 0:
        print_n(n - 1)
        print(n,end=" ")
print_n(5)'''

#printing the string reverse
s= " why are you shy"
def reverse_string_recursion(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse_string_recursion(s[:-1])

reversed_string = reverse_string_recursion(s)
print(reversed_string)



