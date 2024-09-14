import threading
from time import sleep
import random


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        self.locked = False

    def deposit(self):
        for i in range(100):
            with self.lock:
                amount = random.randint(50, 500)

                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance} ", end="\n")
                if self.balance >= 500 and self.locked:
                    self.locked = False
                    self.lock.release()
            sleep(0.001)

    def take(self):
        for _ in range(100):
            with self.lock:
                amount = random.randint(50, 500)
                print(f"Запрос на {amount} ", end="\n")

                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}", end="\n")

                else:
                    print("Запрос отклонён, недостаточно средств")
                    if not self.lock.locked():
                        self.lock.acquire()
            sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')