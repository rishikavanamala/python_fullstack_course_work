password=input("Enter the password:")
if len(password)>=8:
    s=set()
    for i in password:
        if i.isupper():
            s.add("upper")
        elif i.islower():
            s.add("lower")
        elif i.isdigit():
            s.add("digit")
        else:
            s.add("splchar")
    if len(s)==4:
        print("Strong password")
    else:
        print("Weak password\n Password must contain upper,lower,digits and special characters")
else:
    print("Password must contain 8 characters")