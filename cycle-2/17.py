
import operator
dic = {1:50,2:20,3:62,4:9}                                                                                                                                    
sort=sorted(dic.items(),key=operator.itemgetter(1))
print(sort)
sort=dict(sorted(dic.items(),key=operator.itemgetter(1),reverse=True))
print(sort)