file = open(r'C:\Users\rishi\OneDrive\Desktop\hello.txt', 'r')
content = file.read()
print(content)

import csv
with open(r"C:\Users\rishi\OneDrive\Desktop\python_course_work\sample.csv") as file:
    content = csv.reader(file)
    for row in content:
        for col in row:
            print(j)
