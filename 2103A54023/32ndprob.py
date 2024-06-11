#find how many prime numbers which satisfy the property where some prime numbers can be expressed as a sum of consecutive primes
#below is with functions implementation and different method
'''def isPrime(num):
    if num == 0 or num == 1:
        return False
    for deno in range(2,int(num**0.5)+1):
        if num%deno==0:
            return False
    return True
num=int(input())
primeList=[i for i in range(2,num+1) if isPrime(i)]
count,psum=0,primeList[0]
for p in primeList[1:]:
    psum+=p
    if psum>num:
        break
    if isPrime(psum):
        count+=1
print(count) '''      
n = int(input())
l, s, c = [], 0, 0

# Generate list of prime numbers up to n
for i in range(2, n + 1):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        l.append(i)

# Check sums of consecutive primes
for k in range(len(l)):
    s += l[k]
    if s > n:
        break
    for i in range(2, int(s ** 0.5) + 1):
        if s % i == 0:
            break
    else:
        if s <= n:  # Ensure the sum is within the limit n
            c += 1

print(c)
       
    
        