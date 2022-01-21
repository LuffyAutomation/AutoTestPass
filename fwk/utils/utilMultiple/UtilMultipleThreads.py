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
            UtilMultipleThreads.run_threads_by_list(list_func)

    @staticmethod
    def run_same_multiprocessing(func, num):
        list_func = []
        for i in range(1, num + 1):
            list_func.append(multiprocessing.Process(target=func))
            UtilMultipleThreads.run_threads_by_list(list_func)

    @staticmethod
    def run_threads_with_same_func(func, num, args_in=None):
        list_func = []
        for i in range(1, num + 1):
            if args_in is None:
                list_func.append(Thread(target=func))
            else:
                list_func.append(Thread(target=func, args=args_in))
        UtilMultipleThreads.run_threads_by_list(list_func)

    @staticmethod
    def get_run_threads_with_different_arg(func, args_in=None):
        return Thread(target=func, args=args_in)

    @staticmethod
    def run_threads_by_list(list_func):
        processes = range(len(list_func))
        for i in processes:
            list_func[i].start()
        for i in processes:
            list_func[i].join()

    def test1(self, a, b):
        print(a)
        print(b)


if __name__ == '__main__':
    aaaaaa = [1,2,3,4,5]
    aaa = UtilMultipleThreads()
    list_threads = []
    list_threads.append(UtilMultipleThreads.get_run_threads_with_different_arg(aaa.test1, ("2", "3",)))

    UtilMultipleThreads.run_threads_by_list(list_threads)
