class ATM:
    def __init__(self):
        self.current_balance = 500
        
    def check_balance(self):
        print(f"your current balance is {self.current_balance}")

    def deposit(self):
        amount=int(input("enter the amount u want to deposit"))
        self.current_balance+=amount
        print(f"u successfully deposited {amount}")
        print(f"your updated balance is {self.current_balance}")

    def withdraw(self):
        amount=int(input("enter the amount u want to withdraw"))
        if amount>self.current_balance: 
            print("insufficient balance")
        else:
            self.current_balance-=amount
            print("u withdraw successfully")
            print(f"your updated balance is {self.current_balance}")
    def met_exit(self):
        exit()