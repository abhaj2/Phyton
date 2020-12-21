#to check the entered number is +ve or -ve
x=int(input("Enter your number"))
if x>0:
 print("{0} is a positive number".format(x))
elif x==0:
 print("The entered number is zero")
else:
 print("{0} is a negative number".format(x))