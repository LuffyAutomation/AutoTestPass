from UiBaseWebDriverFwk import UiBaseWebDriverFwk
import inspect


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
        element_name = self._getCurrentElementNameWhenNone(element_name)
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

    def __toStr(self, value):
        if type(value) is int or type(value) is long or type(value) is float:
            pass
        elif type(value) is bool:
            if value is True:
                return "True"
            else:
                return "False"
        return value

    def __verifyEqual(self, value, objectValue, func_name=None, element_name=None):
        element_name = self._getCurrentElementNameWhenNone(element_name)
        objectValue = str(objectValue)
        value = str(value)
        global t
        t = "is"
        if "NotEqual" in func_name:
            t = "is not"
        elif "NotContain" in func_name:
            t = "does not contain"
        elif "Contain" in func_name:
            t = "contains"

        objectValue = objectValue.decode("utf-8")
        value = value.decode("utf-8")
        if func_name == "verifyCount":
            self.logger.info("Verify the number of the element(s) [%s] %s [%s]." % (element_name, t, objectValue))  # decode encode for python 2
        else:
            self.logger.info("Verify the value or status of the element [%s] %s [%s]." % (element_name, t, objectValue)) # decode encode for python 2
        if "NotEqual" in func_name:
            if value == objectValue:
                self.logger.info("Failed!")
                raise Exception("The element ['" + element_name + "']'s actual result is ['" + value + "'], but the expected result is [" + objectValue + "] as well.")
        elif "NotContain" in func_name:
            if objectValue in value:
                self.logger.info("Failed!")
                raise Exception("The element ['" + element_name + "']'s actual result ['" + value + "'] that Contain [" + objectValue + "].")
        elif "verifyContain" in func_name:
            if objectValue not in value:
                self.logger.info("Failed!")
                raise Exception("The element ['" + element_name + "']'s actual result ['" + value + "'] that does not contain [" + objectValue + "].")
        elif value != objectValue:
            self.logger.info("Failed!")
            if func_name == "verifyCount":
                raise Exception("The number of element ['" + element_name + "'] is ['" + value + "'], but the expected result is [" + objectValue +"].")
            else:
                raise Exception("The element ['" + element_name + "']'s actual result is ['" + value + "'], but the expected result is [" + objectValue + "].")
        self.logger.info("Passed!")

    def verifyCount(self, value, objectValue, element_name=None):
        self.__verifyEqual(value, objectValue, inspect.stack()[0][3])

    def verifyNotEqual(self, value, objectValue, element_name=None):
        objectValue = self.__boolToStr(objectValue)
        value = self.__boolToStr(value)
        self.__verifyEqual(value, objectValue, inspect.stack()[0][3])

    def verifyEqual(self, value, objectValue, element_name=None):
        objectValue = self.__boolToStr(objectValue)
        value = self.__boolToStr(value)
        self.__verifyEqual(value, objectValue, inspect.stack()[0][3])

    def verifyContain(self, value, objectValue, element_name=None):
        objectValue = str(objectValue)
        value = str(value)
        self.__verifyEqual(value, objectValue, inspect.stack()[0][3])

    def verifyNotContain(self, value, objectValue, element_name=None):
        objectValue = str(objectValue)
        value = str(value)
        self.__verifyEqual(value, objectValue, inspect.stack()[0][3])

    def verifyNotContain(self, value, objectValue, element_name=None):
        objectValue = str(objectValue)
        value = str(value)
        self.__verifyEqual(value, objectValue, inspect.stack()[0][3])

    def verifyChecked(self, value, objectValue=VerifyString.CHECKED, element_name=None):
        value = self.__boolToSpecifiledStr(value, self.VerifyString.CHECKED, self.VerifyString.UNCHECKED)
        self.__verifyEqual(value, objectValue, inspect.stack()[0][3])

    def verifyUnchecked(self, value, objectValue=VerifyString.UNCHECKED, element_name=None):
        value = self.__boolToSpecifiledStr(value, self.VerifyString.CHECKED, self.VerifyString.UNCHECKED)
        self.__verifyEqual(value, objectValue, inspect.stack()[0][3])

    def verifyEnabled(self, value, objectValue=VerifyString.ENABLED, element_name=None):
        value = self.__boolToSpecifiledStr(value, self.VerifyString.ENABLED, self.VerifyString.DISABLED)
        self.__verifyEqual(value, objectValue, inspect.stack()[0][3])

    def verifyDisable(self, value, objectValue=VerifyString.DISABLED, element_name=None):
        value = self.__boolToSpecifiledStr(value, self.VerifyString.ENABLED, self.VerifyString.DISABLED)
        self.__verifyEqual(value, objectValue, inspect.stack()[0][3])

    def verifySelected(self, value, objectValue=VerifyString.SELETED, element_name=None):
        value = self.__boolToSpecifiledStr(value, self.VerifyString.SELETED, self.VerifyString.UNSELETED)
        self.__verifyEqual(value, objectValue, inspect.stack()[0][3])

    def verifyUnselected(self, value, objectValue=VerifyString.UNSELETED, element_name=None):
        value = self.__boolToSpecifiledStr(value, self.VerifyString.SELETED, self.VerifyString.UNSELETED)
        self.__verifyEqual(value, objectValue, inspect.stack()[0][3])

    def isChecked(self, idx_or_match=None, element_name=None):
        return self.__isChecked(False, idx_or_match, element_name)

    def isAllChecked(self, idx_or_match=None, element_name=None):
        return self.__isChecked(True, idx_or_match, element_name)

    def __isChecked(self, isCollection=False, idx_or_match=None, element_name=None):
        try:
            if not isCollection:
                element = self._getElementObjectFromCurrentOrSearch(idx_or_match, element_name)
            else:
                element = self._getElementCollectionObjectFromCurrentOrSearch(idx_or_match, element_name)
            if type(element) is list and isCollection:  # set index = 0 in uimaps
                for ele in element:
                    if "true" not in ele.get_attribute(self.AttributeType.CHECKED):
                        return False
                return True
            elif type(element) is list and not isCollection:
                return False if "true" not in element[0].get_attribute(self.AttributeType.CHECKED) else True
            return True if "true" in element.get_attribute(self.AttributeType.CHECKED) else False
        except Exception as e:
            return False

    def isAllPresent(self, idx_or_match=None, element_name=None):
        return self.__isPresent(True, idx_or_match, element_name)

    def __isPresent(self, isCollection=False, idx_or_match=None, element_name=None):
        try:
            element_name = self._getCurrentElementNameWhenNone(element_name)
            element = self._getElementObjectFromCurrentOrSearch(idx_or_match, element_name)
            if element is None:
                if not isCollection:
                    element = self.getMatchedElement(idx_or_match, element_name)
                else:
                    element = self.getMatchedElements(idx_or_match, element_name)
            if type(element) is list and isCollection:  # set index = 0 in uimaps
                for ele in element:
                    if ele.is_displayed() is False:
                        return False
                return True
            elif type(element) is list and not isCollection:
                return element[0].is_displayed()
            return element.is_displayed()
        except Exception as e:
            return False

    def isPresent(self, idx_or_match=None, element_name=None):
        return self.__isPresent(False, idx_or_match, element_name)

    def isEnabled(self, idx_or_match=None, element_name=None):
        return self.__isEnabled(False, idx_or_match, element_name)

    def isAllEnabled(self, idx_or_match=None, element_name=None):
        return self.__isEnabled(True, idx_or_match, element_name)

    def __isEnabled(self, isCollection=False, idx_or_match=None, element_name=None):
        try:
            if not isCollection:
                element = self._getElementObjectFromCurrentOrSearch(idx_or_match, element_name)
            else:
                element = self._getElementCollectionObjectFromCurrentOrSearch(idx_or_match, element_name)
            if type(element) is list and isCollection:  # set index = 0 in uimaps
                for ele in element:
                    if ele.is_enabled() is False:
                        return False
                return True
            elif type(element) is list and not isCollection:
                return element[0].is_enabled()
            return element.is_enabled()
        except Exception as e:
            return False

    def isSelected(self, idx_or_match=None, element_name=None):
        return self.__isSelected(False, idx_or_match, element_name)

    def isAllSelected(self, idx_or_match=None, element_name=None):
        return self.__isSelected(True, idx_or_match, element_name)

    def __isSelected(self, isCollection=False, idx_or_match=None, element_name=None):
        try:
            if not isCollection:
                element = self._getElementObjectFromCurrentOrSearch(idx_or_match, element_name)
            else:
                element = self._getElementCollectionObjectFromCurrentOrSearch(idx_or_match, element_name)
            if type(element) is list:  # set index = 0 in uimaps
                for ele in element:
                    if ele.is_selected() is False:
                        return False
                return True
            return element.is_selected()
        except Exception as e:
            return False

    def clickIfPresent(self, idx_or_match=None, element_name=None):
        if self.isPresent(idx_or_match, element_name) is True:
            self.click(idx_or_match, element_name)
        return self

