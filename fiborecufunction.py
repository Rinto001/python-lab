def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))
    n=int(input("enter the number"))
    recur_fibo(n)
    for i in range(n):
        print(recur_fibo(i))
        
