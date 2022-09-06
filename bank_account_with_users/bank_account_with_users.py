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
        print ("interest:", self.int_rate*100,'%')
        return self

    def yield_interest(self):
        if self.balance > 0:
            total_with_int = self.balance * self.int_rate
            self.balance = self.balance + total_with_int
        else:    
            print ("invest more")
        return self 

class Users:
    
    def __init__(self, name, email,age,lastname, firstname,accountnumber,balance=0,int_rate=0.1):
        self.name=name
        self.email=email
        self.age=age
        self.lastname=lastname
        self.firstname=firstname
        self.accountnumber=accountnumber
        self.account=BankAccount(balance,int_rate)

    def display_user_info(self):
        print(self.name)
        print(self.email)  
        print(self.age)
        print(self.accountnumber)
        return self

    def make_deposit(self, amount):
        self.account.deposit(amount) 
        print ('Deposit was successful')
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        print ('Withdrawal was successful')
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self        

user1 = BankAccount (0.1, 300).deposit(500).deposit(45).deposit(1000).withdraw(200).yield_interest().display_account_info()
user2 = BankAccount(0.01,750).deposit(100).deposit(2200).withdraw(25).withdraw(75).withdraw(50).withdraw(100).yield_interest().display_account_info()
user3 = BankAccount()


print(user1.balance)
print(user2.balance)