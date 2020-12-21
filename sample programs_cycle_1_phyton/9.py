print("Enter 3 Numbers\n")
x=int(input())
y=int(input())
z=int(input())
if(x>y and x>z):
 print("{0} is the greatest among the given 3 numbers".format(x))
if(y>x and y>z):
 print("{0} is the greatest among the given 3 numbers".format(y))
else:
 print("{0} is the greatest among the given 3 numbers".format(z))