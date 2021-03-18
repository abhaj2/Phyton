f1=open("demo",'r')
f2=open("New", 'w')
count=f1.readlines()
for i in range(0,len(count)):
    if(i%2!=0):
        f2.write(count[i])
f2=open("New",'r')
count1=f2.read()
print(count1)
f2.close()
f1.close()