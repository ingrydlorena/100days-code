'''
Day 90: Concurrency and parallelism
Explore concurrency and parallelism with Python (e.g., threading, multiprocessing).
'''

import threading
import time

def task(name):
    print(f"Task {name} starting")
    time.sleep(2)
    print(f"Task {name} completed")

thread1 = threading.Thread(target=task, args=("A",))
thread2 = threading.Thread(target=task, args=("B",))


thread1.start()
thread2.start()


thread1.join()
thread2.join()

print("All tasks completed")