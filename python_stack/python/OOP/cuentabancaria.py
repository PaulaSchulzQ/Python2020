#Crea una clase de BankAccount con los atributos tasa de interés y saldo
#Agrega un método de depósito a la clase BankAccount
#Agrega un método de retiro a la clase BankAccount
#Agrega un método display_account_info a la clase BankAccount
#Agrega un método yield_interest a la clase BankAccount
#Crea 2 cuentas
#En la primera cuenta, realice 3 depósitos y 1 retiro, luego calcule los intereses y
# muestre la información de la cuenta en una sola línea de código (es decir, encadenamiento)
#En la segunda cuenta, realice 2 depósitos y 4 retiros, luego calcule los intereses
# y muestre la información de la cuenta en una sola línea de código (es decir, encadenamiento)

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
