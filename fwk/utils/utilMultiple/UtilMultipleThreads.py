# coding: utf-8
import multiprocessing
import time


class UtilMultipleThreads:
    def __init__(self, *args):
        pass

    @staticmethod
    def run_multiple_threads(funcs):
        list_func = []
        for func in funcs:
            list_func.append(multiprocessing.Process(target=func))
        processes = range(len(list_func))
        for i in processes:
            list_func[i].start()
            time.sleep(1)
        for i in processes:
            list_func[i].join()
