import sys
from multiprocessing import Process, set_start_method
from threading import Thread
from urllib import request, error
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
    try:
        resp = request.urlopen('http://localhost')
    except error.HTTPError as e:
        print(e.code, e.read())
    except error.URLError as e:
        print(e)
    else:
        print(resp.status, resp.read())


t = Thread(target=sleep)
t.start()
process = Process(target=send, daemon=True)
process.start()
process.join()
t.join()
