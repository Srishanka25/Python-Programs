import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.punctuation)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)

n=input()#check the given number or not
for i in n:
    if i not in string.digits:
        print("False")
        break
else:
    print("True")
        