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

        '''
                time.sleep(2)
                new = self.driver.page_source

                d = difflib.Differ()
                rel = d.compare(old,new)
                print(list(rel))

                a = difflib.SequenceMatcher(a=old, b=new).quick_ratio()
                b = difflib.SequenceMatcher(a=old, b=new).ratio()
                while True:
                    new = self.driver.page_source
                    if difflib.SequenceMatcher(a=old, b=new).quick_ratio() > 0.95:
                        time.sleep(2)
                        new = self.driver.page_source
                        if difflib.SequenceMatcher(a=old, b=new).quick_ratio() > 0.95:
                            break
                    old = new
                    
         def til(method, timeout, poll=1, message=''):
            start_time = datetime.datetime.now()
            while True:
                try:
                    value = method()
                    if value:
                        return value
                except Exception as e:
                    pass
                wait(poll)
                if date_diff(start_time, datetime.datetime.now()) >= timeout:
                    break
            raise Exception("Timeout." + message)


    def date_diff(start_time, current_time, unit="s"):
        t = current_time - start_time
        if unit == 's':
            return t.seconds
        else:
            return t.seconds / 60           
                    
        '''