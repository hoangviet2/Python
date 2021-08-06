class Account:
    
    def __init__(self,filepath):
        self.filepth = filepath
        with open(self.filepth,'r') as file:
            self.balance = float(file.read())

    def withdraw(self,ammount):
        self.balance = self.balance-float(ammount)

    def deposit(self,ammount):
        self.balance = self.balance+float(ammount)

    def commit(self):
        with open(self.filepth,'w') as file:
            file.write(str(self.balance))

class checking(Account):

    def __init__(self,filepth,fee=100):
        Account.__init__(self,filepth)
        self.fee = fee

    def transfer(self,amount):
        self.balance = self.balance-amount-self.fee