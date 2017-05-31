from UiBaseWebDriverFwk import UiBaseWebDriverFwk
from abc import abstractmethod


class UiFwk(UiBaseWebDriverFwk):
    def __init__(self, Init):
        UiBaseWebDriverFwk.__init__(self, Init)

    class VerifyString:
        CHECKED = "checked"
        UNCHECKED = "unchecked"
        ENABLED = "enabled"
        DISABLED = "disabled"
        SELETED = "selected"
        UNSELETED = "unselected"

    def waitForShown(self, time_out=None, idx_or_match=None, element_name=None, verify_shown=True, log_head=None):
        element_name = self._getElementNameFrom(element_name)
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

    def __boolToStr(self, value):
        if type(value) is bool:
            if value is True:
                return "True"
            else:
                return "False"
        return value

    def __boolToSpecifiledStr(self, value, a, b):
        if type(value) is bool:
            if value is True:
                return a
            else:
                return b
        return value

    def __verifyEqual(self, value, expectedValue, func_name=None, element_name=None):
        element_name = self._getElementNameFrom(element_name)
        expectedValue = str(expectedValue)
        value = str(value)
        if func_name == "verifyCount":
            self.logger.info("Verify the number of element [" + element_name + "] is [" + expectedValue.decode("utf-8") + "].")  # decode encode for python 2
        else:
            self.logger.info("Verify the element [" + element_name + "] is [" + expectedValue.decode("utf-8") + "].") # decode encode for python 2
        if value.encode('utf-8') != expectedValue:
            self.logger.info("Failed!")
            if func_name == "verifyCount":
                raise Exception("The number of element ['" + element_name + "'] is ['" + value + "'], but the expected result shall be [" + expectedValue +"].")
            else:
                raise Exception("The element ['" + element_name + "']'s actual result is ['" + value + "'], but the expected result shall be [" + expectedValue + "].")
        else:
            self.logger.info("Passed!")

    def verifyCount(self, value, expectedValue, element_name=None):
        self.__verifyEqual(value, expectedValue, "verifyCount")

    def verifyEqual(self, value, expectedValue, element_name=None):
        expectedValue = self.__boolToStr(expectedValue)
        value = self.__boolToStr(value)
        self.__verifyEqual(value, expectedValue)

    def verifyChecked(self, value, expectedValue=VerifyString.CHECKED, element_name=None):
        value = self.__boolToSpecifiledStr(value, self.VerifyString.CHECKED, self.VerifyString.UNCHECKED)
        self.__verifyEqual(value, expectedValue)

    def verifyUnchecked(self, value, expectedValue=VerifyString.UNCHECKED, element_name=None):
        value = self.__boolToSpecifiledStr(value, self.VerifyString.CHECKED, self.VerifyString.UNCHECKED)
        self.__verifyEqual(value, expectedValue)

    def verifyEnabled(self, value, expectedValue=VerifyString.ENABLED, element_name=None):
        value = self.__boolToSpecifiledStr(value, self.VerifyString.ENABLED, self.VerifyString.DISABLED)
        self.__verifyEqual(value, expectedValue)

    def verifyDisable(self, value, expectedValue=VerifyString.DISABLED, element_name=None):
        value = self.__boolToSpecifiledStr(value, self.VerifyString.ENABLED, self.VerifyString.DISABLED)
        self.__verifyEqual(value, expectedValue)

    def verifySelected(self, value, expectedValue=VerifyString.SELETED, element_name=None):
        value = self.__boolToSpecifiledStr(value, self.VerifyString.SELETED, self.VerifyString.UNSELETED)
        self.__verifyEqual(value, expectedValue)

    def verifyUnselected(self, value, expectedValue=VerifyString.UNSELETED, element_name=None):
        value = self.__boolToSpecifiledStr(value, self.VerifyString.SELETED, self.VerifyString.UNSELETED)
        self.__verifyEqual(value, expectedValue)

    def isChecked(self, idx_or_match=None, element_name=None):
        try:
            element_name = self._getElementNameFrom(element_name)
            element = self._getElementObjectFrom(idx_or_match, element_name)
            if element is None:
                element = self.getMatchedElement(idx_or_match, element_name)
            checkbox_class = element.get_attribute(self.AttributeType.CHECKED)
            if "true" in checkbox_class:
                return True
            else:
                return False
        except Exception as e:
            return False

    def isPresent(self, idx_or_match=None, element_name=None):
        try:
            element_name = self._getElementNameFrom(element_name)
            element = self._getElementObjectFrom(idx_or_match, element_name)
            if element is None:
                element = self.getMatchedElement(idx_or_match, element_name)
            return element.is_displayed()
        except Exception as e:
            return False

    def isEnabled(self, idx_or_match=None, element_name=None):
        try:
            element_name = self._getElementNameFrom(element_name)
            element = self._getElementObjectFrom(idx_or_match, element_name)
            if element is None:
                element = self.getMatchedElement(idx_or_match, element_name)
            return element.is_enabled()
        except Exception as e:
            return False

    def isSelected(self, idx_or_match=None, element_name=None):
        try:
            element_name = self._getElementNameFrom(element_name)
            element = self._getElementObjectFrom(idx_or_match, element_name)
            if element is None:
                element = self.getMatchedElement(idx_or_match, element_name)
            return element.is_selected()
        except Exception as e:
            return False

    def clickIfPresent(self, idx_or_match=None, element_name=None):
        if self.isPresent(idx_or_match, element_name) is True:
            self.click(idx_or_match, element_name)
        return self

