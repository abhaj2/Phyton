import math
list=[]
n1=int(input("Enter your 1st limit\n"))
n2=int(input("Enter your 2st limit\n"))
for i in range(n1,n2):
   root=math.sqrt(i)
   if (i%2==0 and int(root)**2==i): 
     list.append(i)
print("Entered list is",list)





