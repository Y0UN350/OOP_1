class BankAccount(object):

    interestRate = 0.125
    nextAccountNum = 1234

    def __init__(self, name, balance):
        self.name= name
        self.balance=balance
        self.accountNumber= BankAccount.nextAccountNum
        BankAccount.nextAccountNum +=1


    def __str__(self):
        #define how to print bankaccount
        output="Name: "+str(self.name)+"\n"
        output += "AccNum: " + str(self.accountNumber) + "\n"
        output += "Balance: " + str(self.balance) + "\n"
        return output

    def deposit(self, amount):
        self.balance += amount


    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Account " + str(self.accountNumber))
            print("Does not have enough withdraw", amount)

    def transferFunds(self, otherAccount, amount):
        if self.balance >= amount:
            self.balance -= amount
            otherAccount.balance += amount
        else:
            print("Account " + str(self.accountNumber))
            print("Does not have enough to transer to AccoNum", otherAccount.accountNumber)

    def depositInterest(self):
        amount = self.balance * BankAccount.interestRate
        self.deposit(amount)

if __name__== "__main__":

    account1 = BankAccount("younes", 1000)
    account2 = BankAccount("Brandon", 100)
    print(account1)
    #account1.depositInterest()
    account1.transferFunds(account2, 100)
    print(account1)
    # account2= BankAccount("Brandon", 1000000)
    # print(account2)