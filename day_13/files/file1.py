file = open('sample.txt',"r")
content = file.read()
file.close()
print("the file content is ")
print(content)


# open and write
print("second print")
file2 = open('sample.txt',"w")
file2.write("adding line 1")
file2.write("adding line 2")

file2.close()

file3 = open('sample.txt',"r")
content2 = file3.read()
print(content2)

#using with
with open('sample3.txt',"w") as file:
        file.write("new file created by python" )

