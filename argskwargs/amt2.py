class Bank_account:
    def __init__(self,balance):
        self.balance = balance
        self.transaction=[]
    
    def deposit(self, amount):
        # if(amount>0):
        self.balance+=amount
        x=f"Deposited: {amount}\nCurrent Balance: {self.balance}"
        self.transaction.append(x)
        print(self.transaction)
        return x

    def withdraw(self, amount):
        if amount<self.balance:
            self.balance -= amount
            x=f"Credited: {amount} \n Current Balance: {self.balance}"
            self.transaction.append(x)
            return x
        else:
            raise"Invalid withdrawal amount."

    def check_balance(self):
        x = f"Current Balance: {self.balance}"
        return x
    
    def show_transactions(self):
        # for val in self.transaction:
        #     print(val)
        return self.transaction
x = Bank_account(2000)
print(x.deposit(500))
print(x.withdraw(600))
print(x.check_balance())
print(x.show_transactions())