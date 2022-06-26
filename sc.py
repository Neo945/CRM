from time import sleep
import schedule

schedule.every(5).seconds.do(lambda : print("Hello World"))

while True:
    print("Sleeping for 5 seconds")
    schedule.run_pending()
    sleep(1)

schedule.every(5).seconds.do(lambda : print("Hello World2"))