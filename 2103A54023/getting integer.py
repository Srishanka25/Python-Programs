#generate a number from the given string if no
#digit found return 0
#'123av45b78'   ->1234578 ->[int]
'''import string
def get_integers(input_string):
    return [int(char) for char in input_string if char in string.digits]
input_string = "123av45b78"
integers = get_integers(input_string)
print(integers) ''' 

'''import string
n=input()
str=""
for i in n:
    if i in string.digits:
        str+=i
if n=="":
    print('0')
else:
    print(str)'''
    
str1="HUNGRY?"
print(str1.replace('?','.'))
str1
