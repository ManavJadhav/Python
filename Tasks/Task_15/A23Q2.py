######################################################################################################
# Program Name     : BankAccountDemo
# Input            : Account holder name, initial balance, deposit and withdrawal amounts
# Output           : Prints account details, updated balance, and interest amount
# Description      : Demonstrates object-oriented programming by implementing
#                    basic bank account operations such as deposit, withdrawal,
#                    and interest calculation using class variables and methods.
# Author           : Manav Mahadev Jadhav
# Date             : 27/01/2026
######################################################################################################

class BankAccount:
    ROI = 10.5

    def __init__(self,A,B):
        self.Name = A
        self.Amount =  B

    def Display(self):
        print("Account holder name : ",self.Name)
        print("Current balance : ",self.Amount)

    def Deposit(self,AmountDeposit):
        self.Amount += AmountDeposit
    
    def Withdraw(self,AmountWithdraw):
        if(AmountWithdraw <= self.Amount):
            self.Amount -= AmountWithdraw
        else:
            print("Insufficient Balance")
    
    def CalculateIntrest(self):
        self.Intrest = (self.Amount * BankAccount.ROI ) / 100 
        
        return self.Intrest
    
    
def main():
    DepositAmount = 0
    WithdrawAmount = 0
    Ret = 0

    print("-"*50)

    obj1 = BankAccount("Manav",1000)
    obj1.Display()

    print("-"*50)

    DepositAmount = int(input("Enter the Amount you want to deposit : "))
    obj1.Deposit(DepositAmount)
    obj1.Display()

    print("-"*50)
    
    WithdrawAmount = int(input("Enter the Amount you want to withdraw : "))
    obj1.Withdraw(WithdrawAmount)
    obj1.Display()

    print("-"*50)

    Ret = obj1.CalculateIntrest()
    print("Intrest amount is  : ",Ret)

    print("-"*50)

    obj2 = BankAccount("Piyush",10000)
    obj2.Display()

    print("-"*50)

    DepositAmount = int(input("Enter the Amount you want to deposit : "))
    obj2.Deposit(DepositAmount)
    obj2.Display()

    print("-"*50)
    
    WithdrawAmount = int(input("Enter the Amount you want to withdraw : "))
    obj2.Withdraw(WithdrawAmount)
    obj2.Display()

    print("-"*50)

    Ret = obj2.CalculateIntrest()
    print("Intrest amount is  : ",Ret)

    print("-"*50)


if __name__ == "__main__":
    main()