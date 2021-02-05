nbr=int(input("Enter your number\n"))
print("The factors of the entered number are")
for i in range(1,nbr+1):
    if nbr%i==0:
        print(i)


