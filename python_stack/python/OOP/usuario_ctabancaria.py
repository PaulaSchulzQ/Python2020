class User:
    def __init__(self, nombreusuario, email):
        self.name=nombreusuario
        self.email=email
        self.account=BankAccount(int_rate=0.02, balance=0)
    def make_deposit(self, amount):
        self.account.deposit(100)
        
    def make_withdrawal(self, amount):
        if self.account>=amount:
            self.account-=amount
        else:
            print("Saldo insuficiente")
    def display_user_balance(self):
        print(self.name, self.account)
    def transfer_money(self, other_user, amount):
        self.amount.balance -= amount
        other_user.make_deposits(amount)

class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate=int_rate
        self.balance=balance
    def deposit(self, amount):
        self.balance+=amount
        return self
    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance-=amount
        elif self.balance<amount:
            print("Saldo insuficiente: se le descontara $5")
            self.balance-=5
        return self
    def display_account_info(self):
        print("Saldo: ", self.balance)
        return self
    def yield_interest(self):
        if self.balance>0:
            self.balance= self.balance*self.int_rate+self.balance
        return self

cuenta1=BankAccount(0.01, 0)
cuenta2=BankAccount(0.07, 100)

cuenta1.deposit(100).deposit(200).deposit(300).withdraw(50).yield_interest().display_account_info()
cuenta2.deposit(300).deposit(300).withdraw(500).withdraw(50).withdraw(100).withdraw(100).yield_interest().display_account_info()