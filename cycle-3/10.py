def factors(n):
 print("The factors of the entered number are")
 for i in range(1,n+1):
    if n%i==0:
        print(i)
nbr=int(input("Enter your number\n"))
factors(nbr)
