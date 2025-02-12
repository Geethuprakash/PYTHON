def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
number=int(input("Enter a number to find factorial"))
if number<1:
    print("The factorial of the number doesnot exist or negative")
else:
    result=factorial(number)
    print(f"the factorial of the {number} is {result} ")
