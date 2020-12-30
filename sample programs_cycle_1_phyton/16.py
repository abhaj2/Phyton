x=int(input("Enter the first number\n"))
y=int(input("Enter the first number\n"))
if (x>y):
 min=x
else:
 min=y
while (1):
 if(min%x==0 and min%y==0):
  print("LCM of two numbers  is",min)
  break
  min=min+1