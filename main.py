class BankAccount:
    instances = []
    def __init__(self, int_rate, balance): 
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.instances.append(self)

    @classmethod
    def check_instances(cls):
        print(cls.instances)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount>self.balance:
            print("Insufficent funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        x = self.balance
        print(f'Balance: ${x}')
        return self

    def yield_interest(self):
        if self.balance>0:
            self.balance += self.balance*self.int_rate
        return self
# ===============User class=====================
class User:
    def __init__(self):
        self.checking = self.account = BankAccount(int_rate=0.02, balance=0)
        self.num_accounts = [self.checking]

    def make_deposit(self, amount):
        self.checking.deposit(amount)
        return self
    
    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(self.account.display_account_info())
        return self
        
    def transfer_money(self, amount, user):
        self.account.withdraw(amount)
        user.account.deposit(amount)
        return self
        
    def create_new_account(self,int_rate,balance):
        self.x = BankAccount(int_rate,balance)
        self.num_accounts.append(self.x)
    # used for debugging, no need for this function
    def print_accounts(self):
        print(self.num_accounts)

felix = User()
elijah = User()
felix.make_deposit(10000)
felix.transfer_money(50,elijah)
felix.create_new_account(.02,1000)
felix.print_accounts()
print("***************")
elijah.print_accounts()
# BankAccount.check_instances()
felix.display_user_balance()
# elijah.display_user_balance()