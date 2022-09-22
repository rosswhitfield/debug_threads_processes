import sys
from multiprocessing import Process, set_start_method
from urllib import request, error
import json

if sys.platform == 'darwin':
    try:
        set_start_method('fork')
    except RuntimeError:
        # context can only be set once
        pass


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


process = Process(target=send)
process.start()
process.join()
