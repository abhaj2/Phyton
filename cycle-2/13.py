c=[]
x=int(input("Enter the limit of the list\n"))
for i in range(1,x+1):
    a=input("Enter your colors\n")
    c.append(a)
print(c)
print(c[0],c[-1])