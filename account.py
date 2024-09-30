class Account:
    def __init__(self,bal,acc_no):
        self.balance = bal
        self.account_no = acc_no
        
    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"was debited")
        print("Total balance",self.get_balance())
        
        
    def credit(self,amount):  
        self.balance += amount
        print("Rs.",amount,"was creadited")
        print("Total balance",self.get_balance())
        
    def get_balance(self):
        return self.balance
            
        
acc1 = Account(10000,'4mu6780')
acc1.credit(40000)
acc1.debit(1000)        