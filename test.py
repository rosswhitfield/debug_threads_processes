from multiprocessing import Process, set_start_method
from threading import Thread
import time

set_start_method('fork')

def sleep():
    print("Start sleep")
    time.sleep(5)
    print("End sleep")

def send():
    print("Hello world")


t = Thread(target=sleep)
t.start()
process = Process(target=send)
process.start()
process.join()
t.join()
