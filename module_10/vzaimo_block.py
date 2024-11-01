import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def thread_task1():
    lock1.acquire()
    print("thread_task1 lock1 acquired")
    time.sleep(1)
    lock2.acquire()
    print("thread_task1 lock 2 acquired")
    lock2.release()
    lock1.release()

def thread_task2():
    lock2.acquire()
    print("thread_task2 lock2 acquired")
    time.sleep(1)
    lock1.acquire()
    print("thread_task2 lock1 acquired")
    lock1.release()
    lock2.release()


if __name__ == "__main__":
    thread1 = threading.Thread(target=thread_task1)
    thread2 = threading.Thread(target=thread_task2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()