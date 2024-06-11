def gcd(n1, n2):
    if n2 == 0:
        return n1
    else:
        return gcd(n2, n1 % n2)

n1 = int(input())
n2 = int(input())

print(f"{gcd(n1, n2)}")
