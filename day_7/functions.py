'''def function_name(arg1,arg2,arg3):
    #stmts
    return
function_name(p1,p2,p3)'''

#Display student data
'''def student_data(info):
    print(f"Name:{info[0]}")
    print(f"Course:{info[1]}")
    print(f"passedout_year:{info[2]}")
    print("-------End-------")
data=[['Komali','PFS','2026'],['Varsha','JFS','2025'],['Lavanya','DS','2027'],['Rishika','DAS','2024']]
for i in data:
    student_data(i)'''

#Display username
'''def display(user_name,email,password):
    print(f"Username:{user_name}")
    print(f"Email id:{email}")
    print(f"Password:{password}")
    print('\n\n')
display(user_name="Komali",email="komali@gmail.com",password="komali@123")
display(email="komali@gmail.com",user_name="Komali",password="komali@123")
display(email="komali@gmail.com",password="komali@123",user_name="Komali")'''

#Default arguement
'''def display(user_name,email,password,status='Absent'):
    print(f"Username:{user_name}")
    print(f"Email id:{email}")
    print(f"Password:{password}")
    print(f"Status:{status}")
    print('\n\n')
display("Komali","komali@gmail.com","komali@123","Present")'''

#variable length arguement
'''def display(*names):
    for i in names:
        print(i)
    else:
        print("-----End of the list-----")
display('Komali')
display('Sirisha')
display('Lavanya')
display('Sandhya')'''




