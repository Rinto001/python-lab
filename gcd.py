def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
result=gcd(num1,num2)
print("gcd of given numbers are",result)


