#fibonocci series
n=int(input("Enter your limit"))
first=0
temp=0
second=1
print( first)
print( second)
for i in range(1,n+1):
  fibo=first+second
  temp=first
  first=second
  second=fibo
  print(fibo)

