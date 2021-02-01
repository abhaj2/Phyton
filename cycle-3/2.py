def fib(n):
    
    x=1
    y=1
    print(x)
    print(y)
    for i in range(0,n ):
        a=x+y
        x=y
        y=a
        print (a)    

limit=int(input("Enter your limit\n"))
fib(limit)
