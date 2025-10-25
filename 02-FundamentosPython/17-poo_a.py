

class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner
        self.__balance = initial_balance # Encapsulacion
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    def withdraw(self, amount):
        
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Fondos insuficientes o cantidad invalida")
            
    def check_balance(self):
        return f"Saldo actual: {self.__balance}"
    
    
account = BankAccount("Cesar", 1000) # Abstraccion

account.deposit(500)
# account.withdraw(700)

print(account.check_balance())