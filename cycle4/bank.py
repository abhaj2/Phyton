class bank:
    def __init__(self,acnt_no,name,type,bal):
        self.acnt_no=acnt_no
        self.name=name
        self.type=type
        self.bal=bal
        print("Your bank account is created")
        print("Accound Number:",self.acnt_no)
        print("Name :", self.name)
        print("Account Type :", self.type)
        print("Balance :", self.bal)
    def deposit(self):
        amount = float(input('Enter the amount to deposit:'))
        self.bal=self.bal+ amount
        print('Your New Balance =%d' % self.bal)

    def widthdraw(self):
        amount=float(input("Enter the amount to  withdraw"))
        if(amount>self.bal):
           print("withdraw not possible")
        else:
           self.bal=self.bal-amount
        print('Your Balance is =%d' % self.bal)
account=bank(1023,"joey","fixed",20)
account.deposit()
account.widthdraw()

