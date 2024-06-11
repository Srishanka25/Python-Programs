#prime number or not using recursion
'''def prime(n, divisor=2):
    if n <= 2:
        return n == 2
    if n % divisor == 0:
        return False
    if divisor * divisor > n:
        return True
    return prime(n, divisor + 1)

num = int(input())
if num < 2:
    print("Please enter a number greater than 1")
elif prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")'''
    
#2 
'''def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
num = int(input())
if prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")'''
# checking whether a number can be represented as sum of two prime number
'''def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def primenums_sum(n):
    for i in range(2, n):
        j = n - i
        if i != j and is_prime(i) and is_prime(j):
            return "yes"
    return "no"

n = int(input())
print(primenums_sum(n))'''
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def primenums_sum(n):
    '''for i in range(2, n):
        j = n - i
        if i != j and is_prime(i) and is_prime(j):
            return "yes"
    return "no"'''
    l=[i for i in range(2,n+1) if is_prime(i)]
    f=False
    for i in range(len(l)):
        for ele in l[i::-1]:
            if sum([l[i],ele])==n and l[i]!=ele:
                f=True
                break
    if f:
        return "yes"
    else:
        return "no"

n = int(input())
print(primenums_sum(n))

