color=['Red','Orange','blue','yellow','green']
colour=['purple','Red','blue','black']
for x in color:
    for y in colour:
        if(x==y):
         color.remove(x)
print(color)
