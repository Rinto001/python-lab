def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)
num=int(input("enter a number"))
if num>=0:
    print("factorial of number",num, "is",factorial(num))
