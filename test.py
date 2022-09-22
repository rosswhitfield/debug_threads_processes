from multiprocessing import Process
from urllib import request

def send():
    with request.urlopen('http://www.python.org/') as f:
        print(f.read(300))

        
process = Process(target=send)
process.start()
process.join()
