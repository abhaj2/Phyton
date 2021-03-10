class overloading_operator:
    def __init__(self , a ,b ) :
        self.a = a
        self.b = b

    def __str__(self):
        return 'overloading_operator(%d %d)' % (self.a,self.b)
    def __add__(self,other):
        
        return overloading_operator(self.a + other.a, self.b + other.b)
p1 =  overloading_operator(2,1)
p2 = overloading_operator(5,1)
print (p1+p2)