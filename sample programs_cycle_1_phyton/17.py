#To count the number of digits in an integer
c=0
x=int(input("Enter the digit"))
while x!=0:
 x=x//10
 c=c+1
print(c) 