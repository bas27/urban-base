#race_condition
#
# import threading
#
# x = 0
#
# def thread_task():
#     global x
#     x = 0
#     for _ in range(10_000_000):
#         x = x + 1
#
# def main():
#     t1 = threading.Thread(target=thread_task)
#     t2 = threading.Thread(target=thread_task)
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
# for i in range(10):
#     main()
#     print(x)

from threading import Thread, Lock

x = 0
lock = Lock()


def thread_task():
    global x
    for i in range(10_000_000):
        with lock:
            x = x + 1


def main():
    global x
    x = 0
    t1 = Thread(target=thread_task)
    t2 = Thread(target=thread_task)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


for i in range(10):
    main()
    print(x)
