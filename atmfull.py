import time
class Atm:
    c_amt=5000
    def withdraw(self):
        amt=int(input("Enter Amount to withdraw: \n"))
        if amt<Atm.c_amt and amt>0 and amt%100==0:
            print(".........PROCEESING.......")
            time.sleep(2)
            print("Amount withdraw is successfull")
            print("PLEASE COOLECT YOUR CASH")
            print("-------------------------------------------------")
            Atm.c_amt=Atm.c_amt-amt
        else:
            print("Insufficient amount")
            print("-------------------------------------------------")

    def deposit(self):
        ac_no=int(input("Enter your account number: \n"))
        ac_no2=int(input("re-enter your account number: \n"))
        if ac_no==ac_no2:
            dep_amt=int(input("enter amount to deposit:\n"))
            Atm.c_amt=Atm.c_amt+dep_amt
            print("AMOUNT DEPOSITED SUCCESSFULLY")
            print("----------------------------------------------------")
    def balance(self):
        time.sleep(2)
        print("your current balance amount is:\n ",Atm.c_amt)
        print("--------------------------------------------------------")
    def transfer(self):
         ac_no=int(input("Enter Account number to transfer:\n "))
         r_acc=int(input("Re-enter the account number: \n"))
         if ac_no==r_acc:
             T_amt=int(input("enter the amount to transfer:\n "))
             if  T_amt<=Atm.c_amt:
                 print("........PROCESSING.........")
                 time.sleep(2)
                 print("Amount Transfer Succesfull")
                 print("---------------------------------------------------")
                 Atm.c_amt=Atm.c_amt-T_amt
             else:
                 time.sleep(2)
                 print("Insufficient amount")
                 print("-------------------------------------------------")  
                
k=Atm()
print("  \t\t\t\tWELCOME TO HDFC BANK")
password=1234
n=0
while n<3:
    pin=int(input("Enter your PIN"))
    if pin==password:
        time.sleep(1)
        print("--------------------------------------------------------")
        option=int(input("SELECT\n1.WITHDRAW\n2.DEPOSIT\n3.BALANCE\n4.TRANSFER\n"))
        if option==1:
            k.withdraw()
        elif option==2:
            k.deposit()
        elif option==3:
            k.balance()
        elif option==4:
            k.transfer()
        else:
            print("Choose the correct option")
            break
        time.sleep(1)
        opt2=input("Do you want to continue <y or Y>")
        if opt2=='y' or opt2=='Y':
            continue
        else:
            break
    else:
        print("Wrong Password")
        n+=1
else:
        print("Your account is blocked for 24 hours")
        exit()
 
  
        
    
