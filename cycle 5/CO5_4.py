#To read specific rows in a csv file and print them
import csv
f = open("D:/New folder/worksheet.csv",'r')
reader = csv.reader(f) for row in reader:
    print(row)