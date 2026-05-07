class account:
    def __init__(self, balance, acc):
        self.balance=balance
        self.acc=acc

    def deposit(self, amount):
        self.balance=self.balance+amount
        print("balance after deposit:", self.balance)

    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance=self.balance-amount
            print("balance after withdraw:", self.balance)
        else:
            print("insufficient balance")
        

acc1=account(1000, "12345")
acc1.deposit(500)        
acc1.withdraw(200)