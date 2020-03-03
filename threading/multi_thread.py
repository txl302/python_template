import threading
import time

def function1(data):
        while True:
                print(data)
                time.sleep(1)

def function2(data):
        while True:
                print(data)
                time.sleep(2)

thread1 = threading.Thread(target = function1, args = (1,))
thread2 = threading.Thread(target = function2, args = (2,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
