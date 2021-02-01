new=[]
limit=int(input("Enter your limit\n"))
sum=0
for i in range(0,limit):
   list=int(input("Enter your element\n"))
   new.append(list)
   sum=sum+list
print("The entered list is",new)
print("The sum aof all elements in the list is :",sum)
