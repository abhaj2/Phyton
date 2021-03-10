class time:
    def __init__(self,hour, min,sec):
        self.__hour=hour
        self.__min=min
        self.__sec=sec

    def __add__(self, other):
        return  self.__hour+other.__hour, self.__min+other.__min , self.__sec+other.__sec

obj1=time(1,32,50)
obj2=time(2,5,12)
obj3=obj1+obj2
print(obj3)