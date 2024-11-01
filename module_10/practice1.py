import random
import time
from threading import Thread
import queue


class Bulka(Thread):

    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            time.sleep(random.randint(1,5))
            if random.random() > 0.9:
                self.queue.put("Подгорелая булка")
            else:
                self.queue.put("Нормальная булка")


class Kotleta(Thread):

    def __init__(self, queue, count):
        super().__init__()
        self.queue = queue
        self.count = count

    def run(self):
        while self.count:
            bulka = self.queue.get(timeout=10)
            if bulka == "Нормальная булка":
                time.sleep(random.randint(1,5))
                self.count -= 1
            print('булок к приготовлению осталось ', self.count)


queue = queue.Queue()

t1 = Bulka(queue)
t2 = Kotleta(queue, 5)

t1.start()
t2.start()

t1.join()
t2.join()
