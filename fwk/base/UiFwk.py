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
            raise Exception("The element['" + element_name + "'] is" + (" not" if verify_shown else " still") + " found on page['" + self.getCurrentPageName() + "'] in " + str(time_out) + "s.")

    def __verifyIs(self, time_out=None, verify_shownOrNot=True, idx_or_match=None, element_name=None, log_head="Verify"):
        self.logger.info(log_head + " the element [" + element_name + "] is" + ("" if verify_shownOrNot else " not") + " shown on page['" + self.getCurrentPageName() + "'].")
        try:
            self.waitUntil(
                lambda: self.isExistent(idx_or_match, element_name) if verify_shownOrNot else not self.isExistent(idx_or_match, element_name), "NA", time_out
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
        try:
            objectValue = str(objectValue)
        except:
            pass
        try:
            value = str(value)  # 'ascii' codec can't encode character u'\xa9' in position 10: ordinal not in range(128)
        except:
            pass
        try:
            if type(value).__name__ == "unicode":
                value = value.encode("utf-8")
        except:
            pass
        try:
            if type(objectValue).__name__ == "unicode":
                objectValue = value.objectValue("utf-8")
        except:
            pass
        # value is unicode and ov is str
        # value == objectValue.decode("utf-8")
        # value.encode("utf-8") == objectValue
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
                element = self._getCurrentElementObjectOrSearch(idx_or_match, element_name)
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

    def isAllVisible(self, idx_or_match=None, element_name=None):
        return self.__isVisible(True, idx_or_match, element_name)

    def __isVisible(self, isCollection=False, idx_or_match=None, element_name=None):
        try:
            element_name = self._getCurrentElementNameWhenNone(element_name)
            element = self._getCurrentElementObjectOrSearch(idx_or_match, element_name)
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

    def isVisible(self, idx_or_match=None, element_name=None):
        return self.__isVisible(False, idx_or_match, element_name)

    def isEnabled(self, idx_or_match=None, element_name=None):
        return self.__isEnabled(False, idx_or_match, element_name)

    def isAllEnabled(self, idx_or_match=None, element_name=None):
        return self.__isEnabled(True, idx_or_match, element_name)

    def isExistent(self, idx_or_match=None, element_name=None):
        return self.__isExistent(False, idx_or_match, element_name)

    def __isExistent(self, isCollection=False, idx_or_match=None, element_name=None):
        try:
            if not isCollection:
                element = self._getCurrentElementObjectOrSearch(idx_or_match, element_name)
            else:
                element = self._getElementCollectionObjectFromCurrentOrSearch(idx_or_match, element_name)
            if type(element) is list and isCollection:  # set index = 0 in uimaps
                return True
            elif type(element) is not list and not isCollection and element is not None:
                return True
            return False
        except Exception as e:
            return False

    def __isEnabled(self, isCollection=False, idx_or_match=None, element_name=None):
        try:
            if not isCollection:
                element = self._getCurrentElementObjectOrSearch(idx_or_match, element_name)
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
                element = self._getCurrentElementObjectOrSearch(idx_or_match, element_name)
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

    def clickIfVisible(self, idx_or_match=None, element_name=None):
        if self.isVisible(idx_or_match, element_name) is True:
            self.click(idx_or_match, element_name)
        return self

    def clickIfExistent(self, idx_or_match=None, element_name=None):
        if self.isExistent(idx_or_match, element_name) is True:
            self.click(idx_or_match, element_name)
        return self

    def _getByDirectionUniqueElement(self, uiFwk, idx_or_match=None, direction="Left"):
        element_name_unique = self.CurrentElement.name
        element_unique = self._getLastElementObjectOrSearch(None, element_name_unique)
        element_unique_location = element_unique.location
        element_unique_x = element_unique_location["x"]
        element_unique_y = element_unique_location["y"]

        element_name = self.LastElement.name
        element_collection = self.getMatchedElements(idx_or_match, self.LastElement.name)

        dict_closest_elements = {}

        # for ele in element_collection:
        for i in range(len(element_collection)):
            ele_location = element_collection[i].location
            ele_x = ele_location["x"]
            ele_y = ele_location["y"]
            if direction.lower() == "left" and ele_x > element_unique_x:
                dict_closest_elements[i] = abs(ele_y - element_unique_y)
            elif direction.lower() == "right" and ele_x < element_unique_x:
                dict_closest_elements[i] = abs(ele_y - element_unique_y)
            elif direction.lower() == "upper" and ele_y > element_unique_y:
                dict_closest_elements[i] = abs(ele_x - element_unique_x)
            elif direction.lower() == "lower" and ele_y < element_unique_y:
                dict_closest_elements[i] = abs(ele_x - element_unique_x)
        dict_closest_elements = sorted(dict_closest_elements.items(), lambda x, y: cmp(x[1], y[1]))
        try:
            index = dict_closest_elements[self.CurrentElementCollection.index - 1][0]
            self.CurrentElement.name = element_name
            self.CurrentElement.page_name = self.LastElement.page_name
            self.CurrentElement.page_uiMap = self.LastElement.page_uiMap
            self.CurrentElement.object = element_collection[index]  # for adding wait for shown, etc
            return self.CurrentElement.object
        except:
            raise Exception("Failed to find element [" + str(element_name) + "] with index [" + str(
                self.LastElement.index) + "] from " + direction + " element [" + element_name_unique + "] on page [" + str(self.getCurrentPageName()) + "].")

    def getByLeftUniqueElement(self, uiFwk, idx_or_match=None):
        self._getByDirectionUniqueElement(uiFwk, idx_or_match, "Left")
        return self
    def getByRightUniqueElement(self, uiFwk, idx_or_match=None):
        self._getByDirectionUniqueElement(uiFwk, idx_or_match, "Right")
        return self
    def getByUpperUniqueElement(self, uiFwk, idx_or_match=None):
        self._getByDirectionUniqueElement(uiFwk, idx_or_match, "Upper")
        return self
    def getByLowerUniqueElement(self, uiFwk, idx_or_match=None):
        self._getByDirectionUniqueElement(uiFwk, idx_or_match, "Lower")
        return self

    def _getNearbyXpathList(self, _list, _value_nearby_, value, _index):
        if not _value_nearby_.strip().startswith("//"):
            _value_nearby_ = "//*" + _value_nearby_
        _list.append({self.Locator.TYPE: "xpath", self.Locator.VALUE: _value_nearby_ + "/parent::*/following-sibling::*/" + value + "[%s]" % _index, self.Locator.INDEX: "1"})
        _list.append({self.Locator.TYPE: "xpath", self.Locator.VALUE: _value_nearby_ + "/parent::*/child::*" + value + "[%s]" % _index, self.Locator.INDEX: "1"})
        _list.append({self.Locator.TYPE: "xpath", self.Locator.VALUE: _value_nearby_ + "/parent::*/" + value + "[%s]" % _index, self.Locator.INDEX: "1"})
        return _list

    def _transformLocatorTypeToXpathStyle(self, locator_type):
        if self.Init.testType.lower() == self.Init.TestType.IOS.lower():
            if locator_type == self.LocatorType.ACCESSIBILITY_ID or locator_type == self.LocatorType.NAME or locator_type == self.LocatorType.TEXT:
                locator_type = self.LocatorType.NAME
        elif self.Init.testType.lower() == self.Init.TestType.ANDROID.lower():
            if locator_type == self.LocatorType.ACCESSIBILITY_ID:
                locator_type = self.LocatorType.CONTENT_DESC
            elif locator_type == self.LocatorType.TEXT:
                locator_type = self.LocatorType.VALUE
            elif locator_type == self.LocatorType.ID:
                locator_type = self.LocatorType.RESOURCE_ID
        return locator_type

    def _transformLocatorValueToXpathStyleForNearby(self, dict_type_value):
        # if dict_type_value[self.Locator.TYPE] != self.LocatorType.XPATH:
        if "[@" not in dict_type_value[self.Locator.VALUE]:
            dict_type_value[self.Locator.VALUE] = "[@%s = '%s']" % (self._transformLocatorTypeToXpathStyle(dict_type_value[self.Locator.TYPE]), str(dict_type_value[self.Locator.VALUE]))
        return dict_type_value

    def _getLocatorListByNearbyUniqueElement(self, element_name, locators_list, locators_list_nearby, idx_or_match=None):
        new_locators_list = []
        for locatorList_nearby in locators_list_nearby:
            dict_type_value_nearby = self._changeCutomizedToOriginal(locatorList_nearby[self.Locator.TYPE], locatorList_nearby[self.Locator.VALUE])
            dict_type_value_nearby = self._transformLocatorValueToXpathStyleForNearby(dict_type_value_nearby)

            locator_value_nearby = dict_type_value_nearby[self.Locator.VALUE] + "[%s]" % locatorList_nearby[self.Locator.INDEX]
            for locatorList in locators_list:
                dict_type_value = self._transformLocatorValueToXpathStyleForNearby(locatorList)
                locator_type = dict_type_value[self.Locator.TYPE]
                locator_value = dict_type_value[self.Locator.VALUE]
                locator_index = locatorList[self.Locator.INDEX]
                if locator_type == self._get_native_locator_type(self.LocatorType.CLASS_NAME) or locator_type == self.LocatorType.ID or locator_type == self.LocatorType.ACCESSIBILITY_ID or locator_type == self.LocatorType.CONTENT_DESC:
                    new_locators_list = self._getNearbyXpathList(new_locators_list, locator_value_nearby, locator_value, locator_index)
                # elif locator_type == self.LocatorType.TEXT:
                #     new_locators_list = self.__getNearbyXpathList(new_locators_list, locator_value_nearby, "*[@%s='%s']" % (self.LocatorType.TEXT, locator_value), locator_index)
                # elif locator_type == self.LocatorType.NAME:
                #     new_locators_list = self.__getNearbyXpathList(new_locators_list, locator_value_nearby, "*[@%s='%s']" % (self.LocatorType.NAME, locator_value), locator_index)
                elif locator_type == self.LocatorType.XPATH:
                    try:
                        locator_value = locator_value.split("/")[locator_value.split("/").__len__() - 1]
                    except:
                        pass
                    new_locators_list = self._getNearbyXpathList(new_locators_list, locator_value_nearby, locator_value, locator_index)
                else:
                    new_locators_list = self._getNearbyXpathList(new_locators_list, locator_value_nearby, "*[@%s='%s']" % (locator_type, locator_value), locator_index)
        # self.CurrentElement.object = self._findElementByLocatorsList(element_name, new_locators_list)  # for adding wait for shown, etc
        self.CurrentElement.name = element_name
        self.CurrentElement.list_locators = new_locators_list
        self.CurrentElement.page_name = self.LastElement.page_name
        self.CurrentElement.page_uiMap = self.LastElement.page_uiMap
        return new_locators_list

    def getByNearbyUniqueElement(self, uiFwk, idx_or_match=None):
        new_locators_list = []
        element_name = self.LastElement.name
        locators_list = self._getElementLocatorsDictList(element_name, self.LastElement)
        element_name_nearby = self.getCurrentElementName()
        locators_list_nearby = self._getElementLocatorsDictList(element_name_nearby)
        self._getLocatorListByNearbyUniqueElement(element_name, locators_list, locators_list_nearby, idx_or_match)
        return self

    def __swipeOrDragDrop(self, uiFwk, left_offset_destination=0, right_offset_destination=0, up_offset_destination=0, down_offset_destination=0, idx_or_match_destination=None, left_offset=0, right_offset=0, up_offset=0, down_offset=0, idx_or_match=None, element_name=None):
        element_name_destination = self.getCurrentElementName()
        element_name = self.LastElement.name

        element = self._getLastElementObjectOrSearch(idx_or_match, element_name)  # put here before getting element_destination since maybe the element object has existed.
        element_destination = self._getCurrentElementObjectOrSearch(idx_or_match_destination, element_name_destination)

        fromXY = self.getElementCenterLocation(left_offset, right_offset, up_offset, down_offset, idx_or_match, self.LastElement)
        fromX = fromXY['x']
        fromY = fromXY['y']
        toXY = self.getElementCenterLocation(left_offset_destination, right_offset_destination, up_offset_destination, down_offset_destination, idx_or_match, self.CurrentElement)
        toX = toXY['x']
        toY = toXY['y']

        return [fromX, fromY, toX, toY]

    def swipeToElement(self, uiFwk, duration=None, left_offset_destination=0, right_offset_destination=0, up_offset_destination=0, down_offset_destination=0, idx_or_match_destination=None, left_offset=0, right_offset=0, up_offset=0, down_offset=0, idx_or_match=None, element_name=None):
        fromTo = self.__swipeOrDragDrop(uiFwk, left_offset_destination, right_offset_destination, up_offset_destination, down_offset_destination, idx_or_match_destination, left_offset, right_offset, up_offset, down_offset, idx_or_match, element_name)
        self.swipe(fromTo[0], fromTo[1], fromTo[2], fromTo[3], duration)
        return self

    def dragToElement(self, uiFwk, duration=None, left_offset_destination=0, right_offset_destination=0, up_offset_destination=0, down_offset_destination=0, idx_or_match_destination=None, left_offset=0, right_offset=0, up_offset=0, down_offset=0, idx_or_match=None, element_name=None):
        fromTo = self.__swipeOrDragDrop(uiFwk, left_offset_destination, right_offset_destination, up_offset_destination, down_offset_destination, idx_or_match_destination, left_offset, right_offset, up_offset, down_offset, idx_or_match, element_name)
        self.drag(fromTo[0], fromTo[1], fromTo[2], fromTo[3], duration)
        return self

    def dragToElementByNative(self, uiFwk, idx_or_match_destination=None, idx_or_match=None, element_name=None):
        element_name_destination = self.getCurrentElementName()
        element_name = self.LastElement.element_name
        element = self._getLastElementObjectOrSearch(idx_or_match, element_name)  # put here before getting element_destination since maybe the element object has existed.
        element_destination = self._getCurrentElementObjectOrSearch(idx_or_match_destination, element_name_destination)
        self._dragByNative(element, element_destination)
        return self

    def drag(self, fromX, fromY, toX, toY, duration=None, width=None, height=None):
        if duration is None:
            duration = 5000  # if use 100, the consecutive second swipe may work abnormally.
            if self.testType.lower() == 'ios':
                duration = 500  # 50 > swipe  500 drag
        else:
            duration = duration * 1000
        if toY > fromY:
            toY += 10
        if toY < fromY:
            toY -= 10
        if toX > fromX:
            toX += 10
        if toX < fromX:
            toX -= 10
        self.swipe(fromX, fromY, toX, toY, duration/1000.0, width, height, "Drag")
        return self

    def swipe(self, fromX, fromY, toX, toY, duration=None, width=None, height=None, logBegin="Swipe"):
        if width is None or height is None:
            size = self.getWindowSize()
        if width is None:
            width = size['width']
        if height is None:
            height = size['height']
        if duration is None:
            duration = 1000  # if use 100, the consecutive second swipe may work abnormally.
            if self.testType.lower() == 'ios':
                duration = 50  # 50 > swipe  500 drag
        else:
            duration = duration * 1000
        self.logger.info("%s from [%s, %s] to [%s, %s]. Screen Width[%s], Screen Height[%s], Duration[%s]." % (logBegin, fromX, fromY, toX, toY, width, height, duration/1000.0))
        if self.testType.lower() == 'ios':
            # toX = 0  # toX should be 0 in ios. Then toX == fromX
            # toY = -100
            self.swipeByNative(fromX, fromY, toX - fromX, toY - fromY, duration)
        else:
            fromX = self.__handleAndroidCoordinate(fromX, width)
            fromY = self.__handleAndroidCoordinate(fromY, height)
            toX = self.__handleAndroidCoordinate(toX, width)
            toY = self.__handleAndroidCoordinate(toY, height)
            self.swipeByNative(fromX, fromY, toX, toY, duration)
        return self
    # for android coordinate
    def __handleAndroidCoordinate(self, num, wOrH):
        if num <= 0:
            num = 1
        if num >= wOrH:
            num = wOrH - 1
        return num

    def swipeDownFromTop(self, move_offset_percent=20, top_offset_percent=0, duration=None, width=None, height=None):
        if width is None or height is None:
            size = self.getWindowSize()
        if width is None:
            width = size['width']
        if height is None:
            height = size['height']
        self.logger.info("Swipe down %s%% from the top. %s%% away from the top" % (move_offset_percent, top_offset_percent))
        self.swipe(width / 2, height / 100.0 * top_offset_percent, width / 2, height / 100.0 * top_offset_percent + height / 100.0 * move_offset_percent, duration, width, height)
        return self

    def swipeDownFromTopToBottom(self, top_offset_percent=0, bottom_offset_percent=0, duration=None, width=None, height=None):
        if width is None or height is None:
            size = self.getWindowSize()
        if width is None:
            width = size['width']
        if height is None:
            height = size['height']
        self.logger.info("Swipe down from the top to bottom. %s%% away from the top to %s%% away from the bottom." % (top_offset_percent, bottom_offset_percent))
        self.swipe(width / 2, height / 100.0 * top_offset_percent, width / 2, height - height / 100.0 * bottom_offset_percent, duration, width, height)
        return self

    def swipeUntilFound_DownFromMid(self, swipe_times=7, move_offset_percent=20, mid_offset_percent=0, duration=None, idx_or_match=None, element_name=None):
        for index in range(swipe_times):
            if self.isVisible(idx_or_match, element_name):
                return self
            self.swipeDownFromMid(move_offset_percent, mid_offset_percent, duration, swipe_times).wait(1)
        raise Exception("Failed to find element [" + element_name + "] on page [" + str(self.CurrentElement.page_name) + "].")

    def swipeUntilFound_UpFromMid(self, swipe_times=7, move_offset_percent=20, mid_offset_percent=0, duration=None, idx_or_match=None, element_name=None):
        for index in range(swipe_times):
            if self.isVisible(idx_or_match, element_name):
                return self
            self.swipeUpFromMid(move_offset_percent, mid_offset_percent, duration, swipe_times).wait(1)
        raise Exception("Failed to find element [" + element_name + "] on page [" + str(self.CurrentElement.page_name) + "].")

    def swipeDownFromMid(self, move_offset_percent=20, mid_offset_percent=0, duration=None, width=None, height=None):
        if width is None or height is None:
            size = self.getWindowSize()
        if width is None:
            width = size['width']
        if height is None:
            height = size['height']
        self.logger.info("Swipe down %s%% from the mid. %s%% away from the mid." % (move_offset_percent, mid_offset_percent))
        self.swipe(width / 2, height / 2 + height / 100.0 * mid_offset_percent, width / 2, height / 2 + height / 100.0 * mid_offset_percent + height / 100.0 * move_offset_percent, duration, width, height)
        return self

    def swipeUpFromBottom(self, move_offset_percent=20, bottom_offset_percent=0, duration=None, width=None, height=None):
        if width is None or height is None:
            size = self.getWindowSize()
        if width is None:
            width = size['width']
        if height is None:
            height = size['height']
        self.logger.info("Swipe up %s%% from the bottom. %s%% away from the bottom." % (move_offset_percent, bottom_offset_percent))
        self.swipe(width / 2, height - height / 100.0 * bottom_offset_percent, width / 2, height - height / 100.0 * bottom_offset_percent - height / 100.0 * move_offset_percent, duration, width, height)
        return self

    def swipeUpFromBottomToTop(self, top_offset_percent=0, bottom_offset_percent=0, duration=None, width=None, height=None):
        if width is None or height is None:
            size = self.getWindowSize()
        if width is None:
            width = size['width']
        if height is None:
            height = size['height']
        self.logger.info("Swipe up from the bottom to top. %s%% away from the top to %s%% away from the bottom." % (top_offset_percent, bottom_offset_percent))
        self.swipe(width / 2, height - height / 100.0 * bottom_offset_percent, width / 2, height / 100.0 * top_offset_percent, duration, width, height)
        return self

    def swipeUpFromMid(self, move_offset_percent=20, mid_offset_percent=0, duration=None, width=None, height=None):
        if width is None or height is None:
            size = self.getWindowSize()
        if width is None:
            width = size['width']
        if height is None:
            height = size['height']
        self.logger.info("Swipe up %s%% from the mid. %s%% away from the mid." % (move_offset_percent, mid_offset_percent))
        self.swipe(width / 2, height / 2 - height / 100.0 * mid_offset_percent, width / 2, height / 2 - height / 100.0 * mid_offset_percent - height / 100.0 * move_offset_percent, duration, width, height)
        return self

    def swipeLeftFromRight(self, move_offset_percent=20, right_offset_percent=0, duration=None, width=None, height=None):
        self.logger.info("Swipe left %s%% from the right. %s%% away from the right." % (move_offset_percent, right_offset_percent))
        if width is None or height is None:
            size = self.getWindowSize()
        if width is None:
            width = size['width']
        if height is None:
            height = size['height']
        self.swipe(width - width / 100.0 * right_offset_percent, height / 2, width - width / 100.0 * right_offset_percent - width / 100.0 * move_offset_percent, height / 2, duration, width, height)
        return self

    def swipeLeftFromMid(self, move_offset_percent=20, mid_offset_percent=0, duration=None, width=None, height=None):
        self.logger.info("Swipe left %s%% from the mid. %s%% away from the mid." % (move_offset_percent, mid_offset_percent))
        if width is None or height is None:
            size = self.getWindowSize()
        if width is None:
            width = size['width']
        if height is None:
            height = size['height']
        self.swipe(width / 2 - width / 100.0 * mid_offset_percent, height / 2, width / 2 - width / 100.0 * mid_offset_percent - width / 100.0 * move_offset_percent, height / 2, duration, width, height)
        return self

    def swipeRightFromLeft(self, move_offset_percent=20, left_offset_percent=0, duration=None, width=None, height=None):
        self.logger.info("Swipe right %s%% from the left. %s%% away from the left." % (move_offset_percent, left_offset_percent))
        if width is None or height is None:
            size = self.getWindowSize()
        if width is None:
            width = size['width']
        if height is None:
            height = size['height']
        self.swipe(width / 100.0 * left_offset_percent, height / 2, width / 100.0 * move_offset_percent, height / 2, duration, width, height)
        return self

    def swipeRightFromMid(self, move_offset_percent=20, mid_offset_percent=0, duration=None, width=None, height=None):
        self.logger.info("Swipe right %s%% from the mid. %s%% away from the mid." % (move_offset_percent, mid_offset_percent))
        if width is None or height is None:
            size = self.getWindowSize()
        if width is None:
            width = size['width']
        if height is None:
            height = size['height']
        self.swipe(width / 2 + width / 100.0 * mid_offset_percent, height / 2, width / 2 + width / 100.0 * mid_offset_percent + width / 100.0 * move_offset_percent, height / 2, duration, width, height)
        return self