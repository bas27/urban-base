from threading import Thread
from time import sleep


class Knight(Thread):
    enemy = 100

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        count = 0
        while self.enemy > 0:
            self.enemy -= self.power
            count += 1
            print(f"{self.name} сражается {count} день(дня)..., осталось {self.enemy} воинов.")
            sleep(1)
        print(f"{self.name} одержал победу спустя {count} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")
