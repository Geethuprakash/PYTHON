def fibonacci(n):
    fib=[]
    a,b=0,1
    for _ in range(n):
        fib.append(a)
        a,b=b,a+b
    return fib

number=int(input("Enter the number of term in fibonacci series : "))
fib_sequence = fibonacci(number)
print(f"The Fibonacci series for {number} terms is:")
print(fib_sequence)