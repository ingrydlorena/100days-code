'''
Day 42: Class methods
Create a class for a bank account with methods for deposit and withdrawal.
'''

class Bank():

    def __init__(self):
        self.available_balance = 0
        self.limit_account = 0

    def deposit(self):
        self.money = int(input('How much do you want to put? '))
        if self.money:
           self.available_balance += self.money
        return f'your deposit was successful'
    
    def withdrawal(self):
        self.amount = int(input('How much do you want plunder? '))
        if self.amount:
            if self.amount < self.available_balance and self.limit_account < 5:
                self.available_balance -= self.amount
                self.limit_account += 1
                return f'Successful withdrawal, you have {self.available_balance} now'
            else:
                return f'invalid operation, you have {self.limit_account} withdraw'
            
bank = Bank()
while True:
    choice = input('which operation do you want to do?\n[D] deposit\n[W] withdrawal\n[L] leave\n')
    if choice.upper() == 'D':
        print(bank.deposit())
    elif choice.upper() == 'W':
        print(bank.withdrawal())
    elif choice.upper() == 'L':
        break
