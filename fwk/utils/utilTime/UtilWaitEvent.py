import datetime
import time

from fwk.utils.utilTime.UtilTime import UtilTime

from fwk.utils.utilConsole.UtilConsole import UtilConsole

POLL_FREQUENCY = 1  # How long to sleep inbetween calls to the method
IGNORED_EXCEPTIONS = (None,)  # exceptions ignored during calls to the method
#IGNORED_EXCEPTIONS = (NoSuchElementException,)  # exceptions ignored during calls to the method


class UtilWaitEvent:

    def __init__(self, timeout, poll_frequency=POLL_FREQUENCY, holder=None):
        self._UtilConsole = UtilConsole
        self._UtilTime = UtilTime
        self._timeout = timeout
        self._poll = poll_frequency
        self._holder = holder
        # avoid the divide by zero
        if self._poll == 0:
            self._poll = POLL_FREQUENCY

    def until(self, method, message=''):
        """Calls the method provided with the driver as an argument until the \
        return value is not False."""
        screen = None
        stacktrace = None
        start_time = datetime.datetime.now()
        end_time = time.time() + self._timeout
        while True:
            try:
                value = method(self._UtilTime.dateDiff(start_time, datetime.datetime.now()))
                if value:
                    return value
            except Exception as exc:
                raise Exception(exc)
                screen = getattr(exc, 'screen', None)
                stacktrace = getattr(exc, 'stacktrace', None)
            time.sleep(self._poll)
            if time.time() > end_time:
                break
            #self._UtilConsole.println("%ss elaplsed. Timeout is %ss." % (start_time, self._timeout))
        raise Exception("%s in %ds." % (message, self._timeout))
        #raise Exception(message, screen, stacktrace)


    def until_not(self, method, message=''):
        """Calls the method provided with the driver as an argument until the \
        return value is False."""
        end_time = time.time() + self._timeout
        while True:
            try:
                value = method(self._holder)
                if not value:
                    return value
            except Exception:
                return True
            time.sleep(self._poll)
            if time.time() > end_time:
                break
        raise Exception(message)

    # def __reLogForCountDown(self, log, interval):
    #     self.log(log)
    #     self.UtilTime.sleep(interval)
    #
    # def log_countDown(self, log, range_max=30, interval=5, range_min=0):
    #     # reLog = lambda x: self.log(log + " > Time left: %s s." % str(x))
    #     reLog = lambda x: self.__reLogForCountDown(log + " > Time left: %s s." % str(x), interval)
    #     self.UtilTime.countDown(range_max, reLog, interval, range_min)
    #
    # def __HandleWaitEvent(self, method, log):
    #     self.log(log)
    #     method()
    #
    # def bbbb(self):
    #     pass
    #
    # def aaaa(self):
    #     self.waitUntil(
    #         lambda: self.bbbb(), "Cannot find found/find printer screen."
    #     )
    #
    # def waitUntil(self, method, error_message="Wait failed.", time_out=None, poll_frequency=1):
    #     if time_out is None:
    #         try:
    #             time_out = float(self._elementTimeOut)
    #         except Exception:
    #             time_out = 60
    #     HandleWaitEvent(time_out, poll_frequency).until(
    #         lambda start_time: self.__HandleWaitEvent(method, "%ss elapsed. Timeout is %ss." % (start_time, time_out)), error_message
    #     )