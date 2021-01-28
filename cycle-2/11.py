a=int(input("Enter your first number\n"))
b=int(input("Enter your second number\n"))
c=int(input("Enter your third number\n"))
if(a>b and a>c):
    print(a,"is the largest among three numbers")
elif(b>a and b>c):
    print(b,"is the largest among three numbers")   
else:
    print(c,"is the largest among three numbers")
