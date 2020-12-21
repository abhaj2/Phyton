#To find factorial of the given digit
factorial=1
n=int(input("Enter your digit"))
if n>0:
    for i in range(1,n+1):
     factorial=factorial*i
    else:
        print(factorial)
elif n==0:
    print("The factorial is 1")
else:
 print("Factorial does not exits")    

 
