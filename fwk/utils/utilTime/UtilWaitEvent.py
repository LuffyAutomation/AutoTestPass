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
        raise Exception
        # raise Exception(message, screen, stacktrace)

