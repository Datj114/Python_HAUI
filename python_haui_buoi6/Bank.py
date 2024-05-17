class BankAccount:
    def __init__(self,accountNumber,name,number) -> None:
        self.accountNumber=accountNumber
        self.name=name
        self.number = number
    def Deposit(self,money):
        self.number+=money
    def Withdrawal(self,money):
        self.number-=money
    def bankFees(self):
        self.number-= self.number*5/100
    def display(self):
        print(f' tai khoan:{self.accountNumber}, chu tai khoan {self.name} , so du {self.number}')
def inputInfo():
    accountNumber=input('nhap id')
    name=input('name')
    number=int(input('money'))
    return BankAccount(accountNumber,name,number)
b1= BankAccount('id1234','Dat',2222000)
b1.display()
b1.Deposit(100000)
b1.Withdrawal(2000)
b1.bankFees()
b1.display()
b=inputInfo()

b.display()