class rectangle:
    def __init__(self,length, bredth):
        self.__length=length
        self.__bredth=bredth


    def __lt__(self, other):
        return  self.__length+other.__length, self.__bredth+other.__bredth

obj1=rectangle(32,50)
obj2=rectangle(2,5)
obj3=obj1<obj2
print(obj3)