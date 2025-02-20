'''
Day 81: Tasks Scheduler
Schedule tasks using the schedule library.
'''
import schedule
import time

def workout():
    return("Time for workout")
def job()
    return("Time for do your job")
def food()
    return('Eat time!')


schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("08:00").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().day.at("11:00", "Europe/Amsterdam").do(job)
schedule.every().minute.at(":16").do(job)

while True:
    schedule.run_pending()
    time.spleet(1)