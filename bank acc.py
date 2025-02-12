class BankAcc:
    Bank_name = "State bank of india"
    Branch = "Calicut"
    def __init__(self,name,num,type,bal):
        self.name = name
        self.account_number = num
        self.account_type = type
        self.balance = bal
    def display(self):
        print("Bank Name :",__class__.Bank_name)
        print("Branch :",__class__.Branch)
        print("Name :",self.name)
        print("Account Number :",self.account_number)
        print("Account Type :",self.account_type)
        print("Current Balance :",self.balance)
    def deposit(self):
        a = int(input("Enter the amount to deposit : "))
        self.balance+=a
        print(f"Current Balance after deposit is {self.balance} : ")
    def withdraw(self):
        print("Current balance :",self.balance)
        b = int(input("Enter the amount to withdraw : "))
        if b <= self.balance:
            print(f"{b} has been withdraw")
            self.balance-=b
            print(f"current balance is : {self.balance}")
        else:
            print(f"Insufficient balance :{self.balance}")
    def option(self):
        while True:
            opt= int(input("1.Deposit \n2.Withdraw \n3.Display Details\n4.Exit\nEnter your choice : "))
            if opt == 1:
                    self.deposit()
            elif opt == 2:
                    self.withdraw()
            elif opt == 3:
                    self.display()
            else :
                        print("Exiting..!\nMany thanks, happy to assist again!")
                        break
while True:
    pin = int(input("Enter your pin number : "))
    if pin == 1020:
        customer1 = BankAcc("asif", 85236144514, "savings", 5000)
        customer1.display()
        customer1.option()
    elif pin == 1030:
        customer2 = BankAcc("Basam", 56489456146, "savings", 1000)
        customer2.display()
        customer2.option()
    elif pin == 1040:
        customer3 = BankAcc("Aseeb", 446446456, "savings", 10000)
        customer3.display()
        customer3.option()
    elif pin == 1050:
        customer4 = BankAcc("Sinu sangeeth", 916916158156, "current acc", 0)
        customer4.display()
        customer4.option()
    else:
        print("Invalid Pin!,Enter correct Pin number")

