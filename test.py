import sys
from multiprocessing import Process, set_start_method
from urllib import request

if sys.platform == 'darwin':
    try:
        set_start_method('fork')
    except RuntimeError:
        # context can only be set once
        pass

def send():
    with request.urlopen('http://www.python.org/') as f:
        print(f.read(300))

        
process = Process(target=send)
process.start()
process.join()
