dict1 = {}
print("1.register")
print("2.login")
option = int(input("enter the option"))
if option==1:
    email = input("enter the email")
    password = input("enter the password")
    if email in dict1:
        print("sorry it is already exist")
    else:
        dict1[email] = password
elif option==2:
    email= input("enter the email")
    password_new = input("enter the password")
    if email not in dict:
        print("emial not exist")
    else:   
        if dict1[email] ==password_new:
            print("login successs")
        else:
            print("sorry login failed")
        
    
    
    
