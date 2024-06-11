'''def fibonacci_series(n):
    s= []
    a, b = 0, 1
    while len(s) < n:
        s.append(a)
        a, b = b, a + b
    return s

n = int(input("Enter the number of terms in the Fibonacci series: "))
result = fibonacci_series(n)
print(f"The first {n} terms of the Fibonacci series are: {result}")'''

'''def fibonacci(n):
    if n <0:
        return ("Incorrect input")
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(int(input())))'''

fibval=[0,1]
def fib(n):
    if n<0:
        print("Incorrect input")
    elif n <len(fibval):
        return fibval[n]
    fibval.append(fib(n-1)+fib(n-2))
    return fibval[n]
print(fib(int(input())))
