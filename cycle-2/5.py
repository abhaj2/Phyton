x=[]
n=int(input("Enter your limit\n"))
for i in range(0,n):
 a=int(input("Enter your integers\n"))
 if(a>100):
  x.append('over')
 else:
  x.append(a)
print(x)
 