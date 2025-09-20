
class Account:
    def __init__(self, name, age, account_no, balance, pin):
        self.name = name
        self.age = age
        self.account_no = account_no
        self.balance = balance
        self.pin = pin

    def check_balance(self):
        return self.balance

    def credit(self, amount):
        self.balance += amount
        return self.balance

    def debit(self, amount):
        if amount > self.balance:
            return -1
        self.balance -= amount
        return self.balance

    def get_pin(self):
        return self.pin
    
    def change_pin(self, new_pin): 
        self.pin = new_pin
        return self.pin