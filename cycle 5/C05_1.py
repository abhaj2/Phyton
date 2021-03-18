f = open("D:/New folder/py.txt", 'r')
x=[]
read_file=f.readlines()
print(read_file)
x.append(read_file)
print(x)
f.close