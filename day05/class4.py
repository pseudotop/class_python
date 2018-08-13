class BankAccount:
    def __init__(self):
        self.__balance = 0

    def withdraw(self, amount):
        self.__balance -= amount
        print("통장에",amount,"가 입금되었음")
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        print("통장에서",amount,"가 출금되었음")
        return self.__balance
    def __str__(self):
        return '잔고 : %d'%self.__balance

a = BankAccount()
a.deposit(100)
b = BankAccount()
b.deposit(1000)
a.withdraw(10)
print(a)
print(b)
