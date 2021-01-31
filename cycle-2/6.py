#occurance of 'a'

names=["Abha","Anna","Navami","jencaAail","Jayakumar"]
count=0
for x in names:
    
    for i in x:
        
     if('a' in i):
        count=count+1
print("The occurance of 'a'in the list is", count)