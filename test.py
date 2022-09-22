import sys
from multiprocessing import Process, set_start_method
from threading import Thread
import urllib3
import json
import time

if sys.platform == 'darwin':
    try:
        set_start_method('fork')
    except RuntimeError:
        # context can only be set once
        pass

def sleep():
    print("Start sleep")
    time.sleep(5)
    print("End sleep")

def send():
    http = urllib3.PoolManager()
    try:
        resp = http.request('GET', 'http://localhost')
    except Exception as e:
        print(e)


t = Thread(target=sleep)
t.start()
process = Process(target=send)
process.start()
process.join()
t.join()
