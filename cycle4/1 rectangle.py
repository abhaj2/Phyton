class rectangle:
    def __init__(self,length,bredth):
        self.length=length
        self.bredth=bredth
    def area (self):
        ar=self.length*self.bredth
        print("Area:",ar)
    def perimeter(self):
        p=2*(self.length+self.bredth)
        print("Perimeter :",p)
a= float(input("Enter the length "))
b=float(input("Enter the bredth"))
c=rectangle(a,b)
c.area()
d=rectangle(a,b)
d.perimeter()
