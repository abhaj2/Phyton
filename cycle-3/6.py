def frequency(str1):
 dict={}
 for n in str1:
   keys=dict.keys()
   if n in keys:
       dict[n]=dict[n]+1
   else:
        dict[n]=1
 return dict
print(frequency("abha"))