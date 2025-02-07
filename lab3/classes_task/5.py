class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}. New balance: {self.balance}")

    def show_balance(self):
        print(f"Account owner: {self.owner}, Balance: {self.balance}")

# Создаём счёт для пользователя "Alice" с начальным балансом 100

account = Account("Alice", 100)

# Показываем начальный баланс
account.show_balance()

# Делаем несколько депозитов
account.deposit(50)
account.deposit(30)

# Делаем несколько снятий
account.withdraw(80)
account.withdraw(30)

# Показываем итоговый баланс
account.show_balance()