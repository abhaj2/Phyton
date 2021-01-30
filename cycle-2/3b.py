sum=0
n=int(input("Enter your limit:\n"))
for x in range(0,n):
 print("Enter the numbers whose square is to be found")
 num=int(input())
 num=num*num
 print("The square of entered number is:",num)
 sum=sum+num
print("\n The sum of all the square of entered numbers are:\n",sum)
 