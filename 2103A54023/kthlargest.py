#kth largest factor of N
n,k=map(int,input().split())
for deno in range(n,0,-1):
    if n%deno ==0:
        k -= 1
    if k==0:
        print(deno)
        break
if k !=0:
    print('1')
    
#2 using recursion
def find_kth_largest_divisor(n, k, current):
    if current == 0:
        return 1
    if n % current == 0:
        k -= 1
        if k == 0:
            return current

    return find_kth_largest_divisor(n, k, current - 1)

n, k = map(int, input("Enter n and k: ").split())
result = find_kth_largest_divisor(n, k, n)
print(result)

    
        
        
        
        
