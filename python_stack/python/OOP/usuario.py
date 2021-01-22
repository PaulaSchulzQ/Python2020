#Crea un archivo con la clase Usuario, incluidos los métodos __init__ y make_deposit
#Agrega un método make_withdrawal a la clase Usuario
#Agrega un método display_user_balance a la clase Usuario
#Crea 3 instancias de la clase de usuario
#Haz que el primer usuario haga 3 depósitos y 1 retiro y luego muestre su saldo
#Haz que el segundo usuario haga 2 depósitos y 2 retiros y luego muestre su saldo
#Haz que el tercer usuario haga 1 depósitos y 3 retiros y luego muestre su saldo
#BONIFICACIÓN: Agrega un método transfer_money; haga que el primer usuario transfiera dinero 
#al tercer usuario y luego imprima los saldos de ambos usuarios

class User:
    def __init__(self, nombreusuario, email):
        self.name=nombreusuario
        self.email=email
        self.account_balance=0
    def make_deposit(self, amount):
        self.account_balance+=amount
        return self
    def make_withdrawal(self, amount):
        if self.account_balance>=amount:
            self.account_balance-=amount
        else:
            print("Saldo insuficiente")
            return self
    def display_user_balance(self):
        print(self.name, self.account_balance)
        return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
bicho= User("Vicente P", "vicente@python.com")

guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(80).display_user_balance()
print()

monty.make_deposit(200).make_deposit(300).make_withdrawal(250)
monty.display_user_balance()
print()

bicho.make_deposit(500).make_deposit(20).make_withdrawal(50)
bicho.display_user_balance()


