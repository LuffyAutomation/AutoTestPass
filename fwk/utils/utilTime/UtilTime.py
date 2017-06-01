import time
import datetime

class UtilTime:
    @staticmethod
    def getDateTime():
        return datetime.datetime.now()

    @staticmethod
    def getCurrentTime():
        return datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S.%f')

    @staticmethod
    def getCodeTime():
        return datetime.datetime.now().strftime('%Y%m%d_%H%M%S%f')

    @staticmethod
    def getCurrentTime1():
        return time.strftime('%m%d%Y%H%M%S', time.localtime(time.time()))

    @staticmethod
    def dateDiff(intialTime ,currentTime, unit="s"):
        #d0 = datetime.datetime(2014, 2, 11 , 17, 20 , 11)
        t = currentTime - intialTime
        # if isinstance(t, float):
        #     t = datetime.datetime.fromtimestamp(t)
        if unit == 's':
            return t.seconds
        else:
            return t.seconds/60

    @staticmethod
    def getNow():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)

    @staticmethod
    def countDown(range_max=45, method=None, interval=-3, range_min=0):
        positive = 0
        negative = 0
        if interval > 0:
            negative = -interval
            positive = interval
        else:
            negative = interval
            positive = -interval
        for x in range(range_max, range_min, negative):
            method(x)
    # def __reLogForCountDown(self, log, interval):
    #     self.log(log)
    #     self.UtilTime.sleep(interval)
    #
    # def log_countDown(self, log, range_max=30, interval=5, range_min=0):
    #     # reLog = lambda x: self.log(log + " > Time left: %s s." % str(x))
    #     reLog = lambda x: self.__reLogForCountDown(log + " > Time left: %s s." % str(x), interval)
    #     self.UtilTime.countDown(range_max, reLog, interval, range_min)