from threading import Thread
from time import sleep

def threaded_function():
    print "running"
    sleep(1)


if __name__ == "__main__":
    thread = Thread(target = threaded_function )
    thread.start() 
    print "thread finished...exiting"