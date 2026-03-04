data={"komali@gmail.com":"klmn@1234","varsha@gmail.com":"varsha@1234","rishika@gmail.com":"rish@2345","sneha@gmail.com":"sneha@123"}
print('1.Register')
print('2.Login')
ch=int(input("Enter the choice:"))
if ch==1:
    email=input("Enter the email:")
    pwd=input("Enter password:")
    if email in data:
        print(f"Register-Failed\n{email} is already exist")
    else:
        data[email]=pwd
        print(f"Register successfull")
elif ch==2:
    email=input("Enter the email:")
    pwd=input("Enter password:")
    if email in data and data[email]==pwd:
        print(f"Login successful")
    else:
        print("Invalid Login")
else:
    print("Enter the valid choice")
    