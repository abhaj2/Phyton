n=int(input("Enter the limit.\n"))
print("Future leap years from current year are:")
for i in range(2021,n):
  if(i%4==0 or i%400==0 and i%100!=0):
     print(i)
  
  