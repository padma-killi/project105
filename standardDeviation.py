import csv
import math

with open('standardDeviation.csv',newline = '') as f:
    reader = csv.reader(f)
    filedata = list(reader)

data = filedata[0]
def mean (data):
    total = 0
    n = len(data)
    for marks in data:
        total = total+ int  (marks)
    mean = total/n
    return mean
    

    
squared_list = []
for number in data:
    a =  int(number) - mean(data)
    a = a**2
squared_list.append(a)
sum = 0
for i in squared_list:
    sum = sum + i
result = sum/ (len(data)-1) 

std_deviation = math.sqrt(result)
print(std_deviation)
