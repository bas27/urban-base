import queue
from random import randint
from threading import Thread
from time import sleep


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        self.name = name
        super().__init__()

    def run(self):
        sleep(randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = tables

    def guest_arrival(self, *guests): # (прибытие гостей)
        for guest in guests:
            if guest not in [table.guest for table in self.tables]:
                for table in self.tables:
                    if table.guest is None:
                        table.guest = guest
                        guest.start()
                        print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    else:
                        self.queue.put(guest)
                        print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while self.queue.empty() is False or [table.guest for table in self.tables] == [None]:





