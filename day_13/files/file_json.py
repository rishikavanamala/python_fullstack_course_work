 # load is for reading
 #dumpu is for loading

'''import json
with open('sample2.json',"r") as file:
    data = json.load(file)
    print(data)

import json
with open ('demo.json','w')as file:
    data = [
    {"name": "rishika", "rollno": 20},
    {"name": "sneha", "rollno": 30},
    {"name": "ananya", "rollno": 25},
    {"name": "priya", "rollno": 28},
    {"name": "kavya", "rollno": 22},
    {"name": "meera", "rollno": 35},
    {"name": "isha", "rollno": 18}
    ]
    json.dump(data,file,indent =4)
    print("success full completed") 

import json
to read 
with open('demo.json',"r") as file:
    data = json.load(file)
    print(data)
'''



#to appned: read file, append the data then write this append data to the file



import json
with open('demo.json',"r") as file:
    data = json.load(file)
    data.append({
    "name": "aarav",
    "rollno":30
    })
with open('demo.json',"w") as file:
    json.dump(data,file,indent=4)


     
