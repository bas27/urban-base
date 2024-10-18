from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):

        for _ in range(100):
            random_deposit = randint(50, 500)
            self.balance += random_deposit
            print(f"Пополнение: {random_deposit}. Баланс: {self.balance}")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for _ in range(100):
            random_take = randint(50, 500)
            print(f"Запрос на {random_take}")
            if self.balance >= random_take:
                self.balance -= random_take
                print(f"Снятие: {random_take}. Баланс: {self.balance}")
                sleep(0.001)
            elif self.balance < random_take:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()


bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
