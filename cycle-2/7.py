sum1=0
list1=[1,56,4,3,10]
len1=len(list1)
print("Length of list 1 is:\n", len1)
for x in range(0,len(list1)):
    sum1+=list1[x]
print("Sum of list 1 is :\n",sum1)
sum2=0    
list2=[15,4,7,96,23]
len2=len(list2)
print("Length of list 2 is:\n",len2)
for y in range(0,len(list2)):
  sum2=sum2+list2[y]
print("Sum of list 2 is :\n", sum2)
if(len1==len2):
    print("The length of both the list are the same")
else:
    print("The length of both the list are not the same")
if(sum1==sum2):
    print("The sum of both the list are same ")    
else:
     print("The sum of both the list are not same ")
if(x in list1[x]==y in list2[y]):
     print("same")
else:
     print("not")