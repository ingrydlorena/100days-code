<<<<<<< HEAD
<<<<<<< HEAD
directory = r'C:\Users\Ingryd\OneDrive\Área de Trabalho\Todo'
prefix = 'test'
suffix = '_automate'
extension = ".txt"

rename_files(directory, prefix, suffix, extension)
=======
'''
Day 81: Tasks Scheduler
Schedule tasks using the schedule library.
'''
import schedule
import time

=======
'''
Day 81: Tasks Scheduler
Schedule tasks using the schedule library.
'''
import schedule
import time

>>>>>>> 09695d39dceeaad3fc2acdbd7c48113468752c12
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
<<<<<<< HEAD
    time.spleet(1)
>>>>>>> e76199ee9c3f8798679760e5bcee589ad6049de0
=======
    time.spleet(1)
>>>>>>> 09695d39dceeaad3fc2acdbd7c48113468752c12
