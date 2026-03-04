data={123456:{'pin':1234,'balance':5000,'history':[]},
      234561:{'pin':2341,'balance':10000,'history':[]},
      342345:{'pin':9856,'balance':20000,'history':[]}}
def check_balance(acc):
    print(f"Your Balance amount is ${data[acc]['balance']}")
def deposit(acc):
    amount=int(input("Enter the amount:"))
    data[acc]['balance']+=amount
    data[acc]['history'].append(f"{amount} is deposited")
    print(f"{amount} is deposited successfully")
def withdraw(acc):
    amount=int(input("Enter the amount:"))
    if amount<=data[acc]['balance']:
        data[acc]['balance']-=amount
        data[acc]['history'].append(f"{amount} is withdraw")
        print(f"{amount} is withdraw successfully")
    else:
        print(f"ou don't have balance")
def view_history(acc):
    if data[acc]['history']:
        print("------Trancaction history------")
        for i in data[acc]['history']:
            print(i)
        else:
            print("-----End of history-----")
    else:
        print("No Transactions")
def menu():
    print('1.Check balance')
    print('2.Deposit')
    print('3.Withdraw')
    print('4.Set pin')
    print('5.View transaction')
    print('6.Exit\n')
print("Welcome to the ATM")
acc=int(input("Enter the account number:"))
pin=int(input("Enter the pin:"))
if acc in data and data[acc]['pin']==pin:
    print("Login Successful")
    while True:
        menu()
        choice=int(input("Enter the choice:"))
        if choice==1:
            check_balance(acc)
        elif choice==2:
            deposit(acc)
        elif choice==3:
            withdraw(acc)
        elif choice==5:
            view_history(acc)
        elif choice==6:
            print("Thankyou")
            break
else:
    print("Invalid Login.Try Again")
            