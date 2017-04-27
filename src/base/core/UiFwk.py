from UiBaseWebDriverFwk import UiBaseWebDriverFwk
from abc import abstractmethod


class UiFwk(UiBaseWebDriverFwk):
    def __init__(self, Init):
        UiBaseWebDriverFwk.__init__(self, Init)

    def waitForShown(self, time_out=None, idx_or_match=None, element_name=None, verify_shown=True, log_head=None):
        element_name = self.getElementNameFrom(element_name)
        if log_head == None: log_head = self._LogHead.WAITINGFOR
        if time_out == None:
            try:
                time_out = float(self._elementTimeOut)
            except Exception:
                time_out = 60
        returnValue= self.__verifyIs(time_out, verify_shown, idx_or_match, element_name, log_head)
        if returnValue == True:
            if log_head == self._LogHead.VERIFY:
                self.logger.info("Passed!")
            return self
        else:
            if log_head == self._LogHead.VERIFY:
                self.logger.info("Failed!")
            raise Exception("The element['" + element_name + "'] is" + (" not" if verify_shown else " still") + " found on page['" + self.getCurrentPage() + "'] in " + str(time_out) + "s.")

    def __verifyIs(self, time_out=None, verify_shownOrNot=True, idx_or_match=None, element_name=None, log_head="Verify"):
        self.logger.info(log_head + " that the element [" + element_name + "] is" + ("" if verify_shownOrNot else " not") + " shown on page['" + self.getCurrentPage() + "'].")
        try:
            self.waitUntil(
                lambda: self.isPresent(idx_or_match, element_name) if verify_shownOrNot else not self.isPresent(idx_or_match, element_name), "NA", time_out
            )
        except Exception as e:
            self.logger.info("The element [" + element_name + "] is not found in " + str(time_out)+"s of timeout.")
            return False
        return True

    def verifyIsNotShown(self, time_out=None, idx_or_match=None, element_name=None):
        return self.waitForShown(time_out, idx_or_match, element_name, False, self._LogHead.VERIFY)

    def verifyIsShown(self, time_out=None, idx_or_match=None, element_name=None):
        return self.waitForShown(time_out, idx_or_match, element_name, True, self._LogHead.VERIFY)

    def verifyEqual(self, value, expectedValue, element_name=None):
        element_name = self.getElementNameFrom(element_name)
        self.logger.info("Verify the element [" + element_name + "]'s value is [" + expectedValue.decode("utf-8") + "].") # decode encode for python 2
        if value.encode('utf-8') != expectedValue:
            self.logger.info("Failed!")
            raise Exception("The element ['" + element_name + "']'s actual value is ['" + value + "'], but the expected value shall be [" + expectedValue +"].")
        else:
            self.logger.info("Passed!")

    def isPresent(self, idx_or_match=None, element_name=None):
        try:
            element_name = self.getElementNameFrom(element_name)
            element = self.getElementObjectFrom(idx_or_match, element_name)
            if element is None:
                element = self.getMatchedElement(idx_or_match, element_name)
            return element.is_displayed()
        #except (IndexError, AttributeError, NoSuchElementException) as e:
        except Exception as e:
            return False

    def clickIfPresent(self, idx_or_match=None, element_name=None):
        if self.isPresent(idx_or_match, element_name) is True:
            self.click(idx_or_match, element_name)
        return self

