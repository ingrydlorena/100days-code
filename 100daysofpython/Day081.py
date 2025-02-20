'''
Day 81: Tasks Scheduler
Schedule tasks using the schedule library.
'''
import schedule
import time

def workout():
    print("Time for workout")
def job():
    print("Time for do your job")
def food():
    print('Eat time!')


schedule.every(5).seconds.do(workout)
schedule.every(1).minutes.do(job)
schedule.every().hour.at("16:28").do(food)


while True:
    schedule.run_pending()
    time.sleep(1)