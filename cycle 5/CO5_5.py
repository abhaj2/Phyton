f = open("D:/New folder/worksheet.csv","r")
import json
thisdict = {
"Name" : "achu",
"Class" : "Jobless",
"Mark" : 851
}
result=json.dumps(thisdict)
f.write(result)
f.close()
f = open("D:/New folder/worksheet.csv","r")
print(f.read())
