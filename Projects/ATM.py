class Account:
    totalAccounts = 1000
    def __init__(self, name, pin, balance=0, accType="Savings"):
        Account.totalAccounts += 1
        self.accNo = str(Account.totalAccounts)
        self.name = name
        self.__pin = pin
        self.balance = balance
        self.accType = accType
        self.transactions = []
        self.dailyLimit = 20000
        self.withdrawToday = 0

    def verifyPin(self):
        entered = input("Enter PIN : ")
        if (entered == self.__pin):
            return True
        else:
            return False

    def deposit(self, amount):
        if (amount <= 0):
            print("Amount should be greater than 0")
            return
        self.balance = self.balance + amount
        txn = len(self.transactions) + 1001
        self.transactions.append(f"Deposit ₹{amount} | Txn ID : {txn}")
        print("Money deposited")

    def withdraw(self, amount):
        if (amount <= 0):
            print("Invalid amount")
            return
        if (amount > self.balance):
            print("Not enough balance")
            return
        if self.withdrawToday + amount > self.dailyLimit:
            print("Daily limit exceeded")
            return
        self.balance -= amount
        self.withdrawToday += amount
        txn = len(self.transactions) + 2001
        self.transactions.append(f"Withdraw ₹{amount} | Txn ID : {txn}")
        print("Please collect cash")

    def transfer(self, receiver, amount):
        if (amount <= 0):
            print("Transfer amount invalid")
            return
        if (amount > self.balance):
            print("Insufficient balance")
            return
        self.balance -= amount
        receiver.balance += amount
        self.transactions.append(f"Sent ₹{amount} to {receiver.name}")
        receiver.transactions.append(f"Received ₹{amount} from {self.name}")
        print("Transfer successful")

    def showBalance(self):
        print("\nCurrent Balance :", self.balance)

    def changePin(self):
        old = input("Old PIN : ")
        if (old != self.__pin):
            print("Wrong old PIN")
            return
        newPin = input("New PIN : ")
        if (len(newPin) != 4):
            print("PIN should be 4 digits")
            return
        self.__pin = newPin
        print("PIN changed")

    def statement(self):
        print("\n------ MINI STATEMENT ------")
        if (len(self.transactions) == 0):
            print("No transactions")
        else:
            for i in self.transactions:
                print(i)

    def details(self):
        print("\n====== ACCOUNT DETAILS ======")
        print("Name :", self.name)
        print("Account Number :", self.accNo)
        print("Account Type :", self.accType)
        print("Balance :", self.balance)

    def saveData(self):
        file = open("accounts.txt", "a")
        file.write(
            self.accNo + "," +
            self.name + "," +
            str(self.balance) + "," +
            self.accType + "\n"
        )
        file.close()

class Bank:

    def __init__(self):
        self.accounts = {}

    def createAccount(self):
        print("\nCreate Account")
        name = input("Enter Name : ")
        if (name == ""):
            print("Name cannot be empty")
            return
        pin = input("Set 4 digit PIN : ")
        if (len(pin) != 4):
            print("PIN must be 4 digits")
            return
        try:
            bal = float(input("Initial Deposit : "))
        except:
            print("Only numbers allowed")
            return
        print("1. Savings")
        print("2. Current")
        typ = input("Choose account type : ")
        accType = "Savings"
        if (typ == "2"):
            accType = "Current"
        acc = Account(name, pin, bal, accType)
        self.accounts[acc.accNo] = acc
        acc.saveData()
        print("\nAccount Created Successfully")
        print("Account Number :", acc.accNo)

    def login(self):
        print("\nLOGIN")
        accNo = input("Enter Account Number : ")
        if (accNo not in self.accounts):
            print("Account not found")
            return
        user = self.accounts[accNo]
        attempts = 3
        while attempts > 0:
            ok = user.verifyPin()
            if (ok):
                print("Login successful")
                self.accountMenu(user)
                return
            else:
                attempts -= 1
                print("Wrong PIN")
                if attempts > 0:
                    print("Attempts left :", attempts)
        print("Too many wrong attempts")
        print("Account blocked")

    def accountMenu(self, user):
        while True:
            print("\n======================")
            print("1 -> Check Balance")
            print("2 -> Deposit")
            print("3 -> Withdraw")
            print("4 -> Transfer")
            print("5 -> Change PIN")
            print("6 -> Statement")
            print("7 -> Account Details")
            print("8 -> Logout")
            print("======================")
            ch = input("Enter option : ")
            if (ch == "1"):
                user.showBalance()
            elif (ch == "2"):
                try:
                    amt = float(input("Amount : "))
                    user.deposit(amt)
                except:
                    print("Invalid input")
            elif ch == "3":
                try:
                    amt = float(input("Enter amount : "))
                    user.withdraw(amt)
                except:
                    print("Numbers only")
            elif ch == "4":
                recv = input("Receiver acc no : ")
                if recv not in self.accounts:
                    print("Receiver not found")
                else:
                    try:
                        amt = float(input("Transfer amount : "))
                        user.transfer(self.accounts[recv],amt)
                    except:
                        print("Invalid amount")
            elif ch == "5":
                user.changePin()
            elif ch == "6":
                user.statement()
            elif ch == "7":
                user.details()
            elif ch == "8":
                print("Logging out...")
                break
            else:
                print("Wrong choice")

    def start(self):
        while True:
            print("\n========= BANK SYSTEM =========")
            print("1. Create Account")
            print("2. Login")
            print("3. Exit")
            choice = input("Select : ")
            if choice == "1":
                self.createAccount()
            elif choice == "2":
                self.login()
            elif choice == "3":
                print("Thanks for using program")
                break
            else:
                print("Enter valid option")
bank = Bank()
bank.start()