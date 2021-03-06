import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
       datefmt="%H:%M:%S")
    logging.info("Main: before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main: before running thread")
    x.start()
    logging.info("Main: wait for the thread to finish")
    # x.join()
    logging.info("Main: all done")

# 输出
root@ubuntu:/home/zp/workspace/pyLearn/thread# python single_thread.py 
19:42:36: Main: before creating thread
19:42:36: Main: before running thread
19:42:36: Thread 1: starting
19:42:36: Main: wait for the thread to finish
19:42:36: Main: all done
19:42:38: Thread 1: finishing
