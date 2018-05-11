# coding: utf-8
import multiprocessing
import time
from threading import Thread

class UtilMultipleThreads:
    def __init__(self, *args):
        pass

    @staticmethod
    def run_different_multiprocessing(funcs):
        list_func = []
        for func in funcs:
            list_func.append(multiprocessing.Process(target=func))
        processes = range(len(list_func))
        for i in processes:
            list_func[i].start()
            time.sleep(1)
        for i in processes:
            list_func[i].join()

    @staticmethod
    def run_same_multiprocessing(func, num):
        list_func = []
        for i in range(1, num + 1):
            list_func.append(multiprocessing.Process(target=func))
        processes = range(len(list_func))
        for i in processes:
            list_func[i].start()
            time.sleep(1)
        for i in processes:
            list_func[i].join()

    @staticmethod
    def _run_thread(list_func):
        processes = range(len(list_func))
        for i in processes:
            list_func[i].start()
            time.sleep(1)
        for i in processes:
            list_func[i].join()

    @staticmethod
    def run_threads_with_same_func(func, num):
        list_func = []
        for i in range(1, num + 1):
            list_func.append(Thread(target=func))
        processes = range(len(list_func))
        for i in processes:
            list_func[i].start()
        for i in processes:
            list_func[i].join()



