class bankaccount:
    def __init__(self):
        self.balance=0
        print("The account is created")

    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Deposit is successful and balance in the account is ",self.balance)
    
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance=self.balance-amount
            print("The withdraw is successful and balance is ", self.balance)
        else:
            print("Insufficient balance")

    def rem_bal(self):
            print("Remaining balance in the account is", self.balance)



