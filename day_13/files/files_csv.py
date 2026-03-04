'''import csv
with open('sample.csv','r') as file:
    data = csv.reader(file)

    for i in data:
        print(i)'''


#append :
import csv
with open('sample.csv','a',newline='\n') as file:
    data = csv.writer(file)
    data.writerow(['10', 'Evalin', '21', 'hyderabad', '90'])

#    for i in data:
 #       print(i)
with open('sample.csv',"r") as file2:
    data = csv.reader(file2)
    for i in data:
        print(i)
 


