'''
Day 90: Concurrency and parallelism
Explore concurrency and parallelism with Python (e.g., threading, multiprocessing).
'''

import multiprocessing
import time

def task(name):
    print(f"Task {name} starting")
    time.sleep(2)
    print(f"Task {name} completed")


if __name__ == "__main__":
    process1 = multiprocessing.Process(target=task, args=("A",))
    process2 = multiprocessing.Process(target=task, args=("B",))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("All task completed")