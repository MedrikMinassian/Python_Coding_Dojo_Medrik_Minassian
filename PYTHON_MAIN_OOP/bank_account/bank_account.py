
class BankAccount:
    
    def __init__(self, int_rate=0.01, balance=0): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance -= 5
            print ('not enough funds')    
        return self    
    def display_account_info(self):
        print ("Balance:", self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        else:
            print ('insufficient funds')
        return self 



account1 = BankAccount (0.1, 300).deposit(500).deposit(45).deposit(800).withdraw(200).yield_interest().display_account_info()
account2 = BankAccount(0.01,750).deposit(100).deposit(2200).withdraw(25).withdraw(75).withdraw(50).withdraw(100).yield_interest().display_account_info()
account3 = BankAccount()
checking = BankAccount()
savings = BankAccount(.1, 30000)