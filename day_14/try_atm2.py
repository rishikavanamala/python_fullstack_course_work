total_amount = 10000
with_draw_list = []
while True:
    print("1. check average")
    print("2 withdraw (with in valid datatype)")
    print("3. deposit (with invalid date)")
    print("4.Acess invalid transaction (indec error) ")
    print("5. Accessing not existing account")
    print("6. read missing transaction log file (file not found)")
    print("7.exit")
    k = int(input("enter your choice"))
    if k==1 :
        print("we are calculation average here: ")
        try :
            sum1 = sum(with_draw_list)
            ave = sum/len(sum1)
            print(f"your avg amount is : {ave}")
        except Exception as E :
            print(f"error occured {E}")
            print("as their are no transctions before this happened")
            
        
    elif k==2:
        print("this is for with drawl")
        try :
            withdraw_amount = int(input("enter the anount u want to with draw"))
            total_amount = total_amount - withdraw_amount
            print("success fully withdraw")
            with_draw_list.append(withdraw_amount)
                    
            
        except Exception as e:
            print("u not entered int")
            print(f"error found {e}")
    elif k==3:
        print("u r depositing here")
        try :
            m = int(input("enter the amount u want to deposite"))
            total_amount = total_amount+m
        except Exception as E:
            print(f"error occured {E}")
            print("u not entered int")
        pass

    elif k==4:
        print("ur accessing the transaction")
        try :
            j = int(input("enter the transaction date u want to acess"))
            print(with_draw_list[j])
        except Exception as E:
            print(E)
        
    elif k==5:
        accounts = 
        

    elif k==6:
        pass

    elif k==7:
        exit


    
    
