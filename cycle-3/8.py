
new=[]
l=int(input("Enter your limit\n" ))
for i in range(0,l):
    string=input("Enter your word\n" )
    print(len(string))
    new.append(string)
    max=len(new[0])
    temp=new[0]
for x in new:
    if(len(x)>max):
       max=len(x)
       temp=x
print("The word with the longest length is:",temp )  

