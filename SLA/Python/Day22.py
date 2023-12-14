class bankaccount:
    def __init__(self):
        self.balance=0
        print("The account is created")

    def __deposit(self):
        amount=int(input("Enter the amount to deposit "))
        self.balance=self.balance+amount
        print("Deposit is successful and balance in the account is ",self.balance)
    
    def __withdraw(self):
        amount=int(input("Enter the amount to withdraw "))
        if self.balance>=amount:
            self.balance=self.balance-amount
            print("The withdraw is successful and balance is ", self.balance)
        else:
            print("Insufficient balance")

    def rem_bal(self):
        self.__deposit()
        self.__withdraw()
        print("Remaining balance in the account is", self.balance)

myobj=bankaccount()
myobj.rem_bal()

# def printdata():
#     acc=bankaccount()

#     while True:
#         n=int(input("Enter the number 1, 2, 3 or 4 "))
#         if n==1:
#             print("Balance", acc.rem_bal())
#         elif n==2:
#             amount=int(input("Enter the amount to deposit"))
#             print(acc.__deposit(amount))
#         elif n==3:
#             amount=int(input("Enter the amount to withdraw "))
#             print(acc.__withdraw(amount))
#         elif n ==4:
#             print("Exiting the ATM. Have a nice day!")
#             break
#         else:
#             print("Invalid choice. Please select a valid option.")

# printdata()