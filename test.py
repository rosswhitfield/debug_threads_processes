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
    time.sleep(10)

def send():
    msgs = {"hello": "world"}
    try:
        req = request.Request("http://localhost",
                              data=json.dumps(msgs).encode(),
                              headers={'Content-Type': 'application/json'},
                              method='POST')
        resp = request.urlopen(req)
    except error.HTTPError as e:
        print(e.code, e.read())
    except error.URLError as e:
        print(e)
    else:
        print(resp.status, resp.read())


def run():
    t = Thread(target=sleep)
    t.start()
    process = Process(target=send)
    process.start()
    process.join()


process = Process(target=run)
process.start()
process.join()
