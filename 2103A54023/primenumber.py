'''def is_prime(n): #checking whether the given number is prime or not
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Test the function
number = int(input())
if is_prime(number):
    print("it is a prime number")
else:
    print("it is not a prime number")
#2
for i in range(2,n):
     if n%i==0:
         print("NOT PRIME")
         break
else:
    print("prime")'''
    
#3
num=int(input())
for deno in range(2,int(num**0.5)+1):
    if num%deno==0:
        print("not prime")
        break
    else:
        print("prime")