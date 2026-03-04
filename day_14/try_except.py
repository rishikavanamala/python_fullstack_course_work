'''
#single try exception
try :
    if a>10:
        print("a was declared and came to try blovk")
        print(a)
except :
    print("their is an error in try it came to except")

a = 10
try :
    if a>=10:
        print("a was declared and came to try blovk")
        print(a)
except :
    print("their is an error in try it came to except") 


#to print an error: 
try :
    if a>=10:
        print("a was declared and came to try blovk")
        print(a)
except Exception as e:
    print("their is an error in try it came to except")
    print(e) 

# multiple error handling:

#we can m=write multiple


try :
    a = int(input())
    if a <0:
        raise Exception("enter the postive val")
    else:
        print("ok")
except Exception as e:
    print(f"error occured {e}")

finally:
    print("end block") '''


