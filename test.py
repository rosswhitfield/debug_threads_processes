from multiprocessing import Process, set_start_method
from urllib import request

set_start_method('fork')

def send():
    with request.urlopen('http://www.python.org/') as f:
        print(f.read(300))

        
process = Process(target=send)
process.start()
process.join()
