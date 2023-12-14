# import BankClass
# def printdata():
#     BankClass.bankaccount()

#     while True:
#         n=int(input("Enter the number 1, 2, 3 or 4 "))
#         if n==1:
#             print( BankClass.rem_bal())
#         elif n==2:
#             amount=int(input("Enter the amount to deposit"))
#             print(BankClass.deposit(amount))
#         elif n==3:
#             amount=int(input("Enter the amount to withdraw "))
#             print(BankClass.withdraw(amount))
#         elif n ==4:
#             print("Exiting the ATM. Have a nice day!")
#             break
#         else:
#             print("Invalid choice. Please select a valid option.")

# printdata()



class ATM:
    def __init__(self):
        self.current_balance=500
        