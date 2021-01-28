n=int(input("Enter your number\n"))
l=int(input("Enter your limit\n"))
m=0
for i in range(1,l+1):
  s=pow(n,i)  
  m=m+s
print(m)  
