import os

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from UiBaseFwk import UiBaseFwk


class UiBaseWebDriverFwk(UiBaseFwk):
    def __init__(self, Init):
        UiBaseFwk.__init__(self, Init)
        if 2 == 1:
            self._driver = webdriver.Remote("")
        # self.Swipe = self._Swipe(self)

    def getDriverOnly(self):
        return self._driver

    def getItemsCount(self):
        try:
            if self.getCurrentElementName() != self.getCurrentElementCollectionName():
                self._getElementObjectFromCurrentOrSearch(None, None)
                self._getCurrentElementNameWhenNone(None)
                return len(self.getCurrentElementCollectionObject())
        except:
            return 0
            # raise Exception("Can not get children count of element [" + self.getCurrentElementCollectionName() + "] on [" + str(self._currentPage) + "] page.")

    def getItems(self):
        try:
            if self.getCurrentElementName() != self.getCurrentElementCollectionName():
                self._getElementCollectionObjectFromCurrentOrSearch(None, None)
                self._getCurrentElementCollectionName(None)
            # self.setCurrentElementName(self.getCurrentElementCollectionName())
            # self.setCurrentElementObject(self.getCurrentElementCollectionObject())
            return self
        except:
            raise Exception("Can not find all of element [" + self.getCurrentElementCollectionName() + "] on [" + str(self._currentPage) + "] page.")

    def getItem(self, child_element_index):
        try:
            if self.getCurrentElementName() != self.getCurrentElementCollectionName():
                self._getElementObjectFromCurrentOrSearch(None, None)
                self._getCurrentElementNameWhenNone(None)
            self.setCurrentElementName(self.getCurrentElementCollectionName() + "_index_" + str(child_element_index))
            self.setCurrentElementObject(self.getCurrentElementCollectionObject()[child_element_index - 1])
            return self
        except:
            raise Exception("Can not find element [" + self.getCurrentElementCollectionName() + "] with index [" + str(child_element_index) + "] on [" + str(self._currentPage) + "] page.")

    def click(self, idx_or_match=None, element_name=None):
        try:
            element = self._getElementObjectFromCurrentOrSearch(idx_or_match, element_name)
            element_name = self._getCurrentElementNameWhenNone(element_name)
            self.logger.info("Click element [" + element_name + "] on [" + str(self._currentPage) + "] page.")
            if element.is_enabled() is True:
                element.click()
            else:
                self.logger.info("The element [" + element_name + "] is not enabled.")
        except NoSuchElementException as e:
            self.logger.error(e)
            raise Exception("Click element [" + element_name + "] failed.")
        return self

    def setValue(self, value, idx_or_match=None, element_name=None):
        try:
            element = self._getElementObjectFromCurrentOrSearch(idx_or_match, element_name)
            element_name = self._getCurrentElementNameWhenNone(element_name)
            self.logger.info("Set the value of element [" + element_name + "] to [" + value + "].")
            self._driver.set_value(element, value)
        except Exception as e:
            self.logger.error("Set the value of element [" + element_name + "] to [" + value + "] failed.")
            raise Exception("Set the value of element [" + element_name + "] to [" + value + "] failed.")
        return self

    def setValueBySendKeys(self, value, idx_or_match=None, element_name=None):
        try:
            element = self._getElementObjectFromCurrentOrSearch(idx_or_match, element_name)
            element_name = self._getCurrentElementNameWhenNone(element_name)
            self.logger.info("Set the value of element [" + element_name + "] to [" + value + "] by sending keys.")
            elementTagName = self._getElementTagName(element)
            if elementTagName == "input" or "text" or "password" or "email":
                try:
                    element.click()
                    element.clear()
                    element.send_keys(value)
                except WebDriverException:
                    element.send_keys(value)
            elif elementTagName == "select":
                select = Select(element)
                select.select_by_visible_text(value)
            elif elementTagName == "checkbox":
                positiveValues = ["y", "yes", "true", "on", "checked"]
                negativeValues = ["n", "no", "false", "off", "unchecked"]
                if positiveValues in value.lower():
                    if not element.is_selected():
                        element.click()
                if negativeValues in value.lower():
                    if element.is_selected():
                        element.click()
        except Exception as e:
            self.logger.error("Set the value of element [" + element_name + "] to [" + value + "] by sending keys failed.")
            raise Exception("Set the value of element [" + element_name + "] to [" + value + "] by sending keys failed.")
        return self

    def _getElementTagName(self, element):
        # get element tar name
        try:
            elementType = element.tag_name
            try:
                elementType += element.get_attribute("type")
            except NoSuchElementException as e:
                pass
            elementType = elementType.lower()
            if ".Select".lower() in elementType:
                elementType = "select"
            elif ".CheckBox".lower() in elementType:
                elementType = "checkbox"
            elif ".Input".lower()in elementType:
                elementType = "input"
            else:
                elementType = "text"
            return elementType
        except Exception as e:
            #raise Exception("get element tag name failed.")
            return "text"

    def getValue(self, attribute_type=None, idx_or_match=None, element_name=None):
        element = self._getElementObjectFromCurrentOrSearch(element_name, idx_or_match)
        return_value = ""
        if self.isPresent(element_name, idx_or_match):
            if attribute_type is None:
                element_type = self._getElementTagName(element)
                if "input" in element_type:
                    return_value = element.get_attribute(self.AttributeType.VALUE)
                elif "text" in element_type:
                    return_value = element.text
                elif "checkbox" in element_type:
                    checkbox_class = element.get_attribute(self.AttributeType.CHECKED)
                    if "true" in checkbox_class:
                        return_value = "checked"
                    else:
                        return_value = "unchecked"
                elif "select" in element_type:
                    for index in range(self.getElementSize(element_name)):
                        select_item = element.find_elements(By.TAG_NAME("option")).get(index)
                        if select_item.is_selected():
                            return_value = select_item.text
                elif return_value is None or return_value == "":
                    return_value = element.text
            else:
                return_value = element.get_attribute(attribute_type)
        return return_value

    def _findElements(self, element_name):
        return self._findElement(element_name, "findElements")

    def _findElement(self, element_name, marks=None):
        locatorsList = self._getElementLocatorsList(element_name)
        ori_element_name = element_name
        for locatorList in locatorsList:
            locator_type = self._getElementType(locatorList)
            locator_value = self._getElementValue(locatorList)
            locator_value = self._getLocatorValueByLocalString(element_name, locator_value)
            if marks == "findElements":
                locator_index = -1
            else:
                locator_index = self._getElementIndex(locatorList)
            try:
                if locator_type == self.LocatorType.ACCESSIBILITY_ID:
                    if locator_index < 0:
                        self.setCurrentElementCollectionName(element_name)
                        self.setCurrentElementCollectionObject(self._driver.find_elements_by_accessibility_id(locator_value))
                        return self.getCurrentElementCollectionObject()
                    elif locator_index == 0:
                        self.setCurrentElementObject(self._driver.find_element_by_accessibility_id(locator_value))
                    else:
                        self.setCurrentElementObject(self._driver.find_elements_by_accessibility_id(locator_value)[locator_index])
                else:
                    if locator_index < 0:
                        self.setCurrentElementCollectionName(element_name)
                        self.setCurrentElementCollectionObject(self._driver.find_elements(locator_type, locator_value))
                        return self.getCurrentElementCollectionObject()
                    elif locator_index == 0:
                        self.setCurrentElementObject(self._driver.find_element(locator_type, locator_value))
                    else:
                        self.setCurrentElementObject(self._driver.find_elements(locator_type, locator_value)[locator_index])
            except Exception as e:
                # traceback.print_exc()
                # print e.__str__()
                continue
            return self.getCurrentElementObject()
        if locator_index < 0:  # When <id/xpath... index="0">android:id/checkbox</id>
            raise Exception("Failed to find all of element [" + str(ori_element_name) + "] on [" + str(self.getCurrentPage()) + "] page.")
        elif locator_index == 0:  # When <id/xpath...>android:id/checkbox</id>
            raise Exception("Failed to find element [" + str(ori_element_name) + "] on [" + str(self.getCurrentPage()) + "] page.")
        else:  # When <id/xpath... index="1/2/3.....">android:id/checkbox</id>
            raise Exception("Failed to find element [" + str(ori_element_name) + "] with index [" + str(locator_index + 1) + "] on [" + str(self.getCurrentPage()) + "] page.")

    # def getElementsSize(self, element_name):
    #     return len(self.getElements(element_name))

    def getMatchedElements(self, match=None, element_name=None):
        return self._findElements(element_name)

    def getMatchedElement(self, idx_or_match=None, element_name=None):
        if idx_or_match is None:
            return self._findElement(element_name)
        elements = self._findElements(element_name)
        if idx_or_match == None:
            if str(type(elements)) == "<class \'appium.webdriver.webelement.WebElement\'>": #accessibility_id    webelement is no len(x)
                return elements
            elif len(elements) == 0:
                raise IndexError("Cannot find element [ " + str(
                    element_name) + "] on [" + str(self._currentPage) + "] page.")
            elif len(elements)!=1:
                raise IndexError("There are multiple matched elements that found, please check element [" + str(element_name) +"] on [" + str(self._currentPage) + "] page.")
            else:
                return elements[0]
        else:
            index = self.__getMatchedIndex(elements, idx_or_match)
            return elements[index]

    def __getMatchedIndex(self, elements, idx_or_match, attribute="text"):
        if isinstance(idx_or_match, int):         # if type(idx_or_match) == type(1):
            return idx_or_match
        index = 0
        getAttText = ""
        if type(idx_or_match) == str:
            for i, element in enumerate(elements):
                if "text" in attribute:
                    getAttText = element.text
                elif ("name" in attribute) or ("content-desc" in attribute):
                    getAttText = element.get_attribute("name")
                if idx_or_match in getAttText:
                    index = i
                    break
        else:
            index = idx_or_match-1
        return index

    def getScreenShot(self, name, Result):
        if self._driver is None:  # debug
            return
        self.wait(1)
        if self.RunTimeConf.isDevicePassTest is True:
            self._driver.get_screenshot_as_file(os.path.join(os.getenv("APPIUM_SCREENSHOT_DIR"), str(Result.getCurrentStep()) + "_" + name + ".png"))
        else:
            self._driver.get_screenshot_as_file(os.path.join(Result.path_folder_testSuiteNumScreenshots, str(Result.getCurrentStep()) + "_" + name + ".png"))
        self.wait(1)
        return os.path.join(Result.path_folder_testSuiteNumScreenshots, str(Result.getCurrentStep()) + "_" + name + ".png")

    def quit(self):
        try:
            if self._driver is not None:
                self._driver.quit()
                self._driver = None
        except Exception as e:
            pass

    def swipeByNative(self, begin_x, begin_y, end_x, end_y, duration=500):
        self._driver.swipe(begin_x, begin_y, end_x, end_y, duration)
        return self

    def swipe(self, fromX, fromY, toX, toY, duration=None, width=None, height=None):
        if width is None:
            width = self.getWindowWidth()
        if height is None:
            height = self.getWindowHeight()
        if duration is None:
            duration = 1000  # if use 100, the continued second swipe may work abnormally.
            if self.testType.lower() == 'ios':
                duration = 100
        else:
            duration = duration * 1000
        self.logger.info("Swipe from [%s, %s] to [%s, %s]. Width[%s], Height[%s], Duration[%s]." % (fromX, fromY, toX, toY, width, height, duration/1000.0))
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
        if width is None:
            width = self.getWindowWidth()
        if height is None:
            height = self.getWindowHeight()
        self.logger.info("Swipe down %s%% from the top. %s%% away from the top" % (move_offset_percent, top_offset_percent))
        self.swipe(width / 2, height / 100.0 * top_offset_percent, width / 2, height / 100.0 * top_offset_percent + height / 100.0 * move_offset_percent, duration, width, height)
        return self

    def swipeDownFromTopToBottom(self, top_offset_percent=0, bottom_offset_percent=0, duration=None, width=None, height=None):
        if width is None:
            width = self.getWindowWidth()
        if height is None:
            height = self.getWindowHeight()
        self.logger.info("Swipe down from the top to bottom. %s%% away from the top to %s%% away from the bottom." % (top_offset_percent, bottom_offset_percent))
        self.swipe(width / 2, height / 100.0 * top_offset_percent, width / 2, height - height / 100.0 * bottom_offset_percent, duration, width, height)
        return self

    def swipeDownFromMid(self, move_offset_percent=20, mid_offset_percent=0, duration=None, width=None, height=None):
        if width is None:
            width = self.getWindowWidth()
        if height is None:
            height = self.getWindowHeight()
        self.logger.info("Swipe down %s%% from the mid. %s%% away from the mid." % (move_offset_percent, mid_offset_percent))
        self.swipe(width / 2, height / 2 + height / 100.0 * mid_offset_percent, width / 2, height / 2 + height / 100.0 * mid_offset_percent + height / 100.0 * move_offset_percent, duration, width, height)
        return self

    def swipeUpFromBottom(self, move_offset_percent=20, bottom_offset_percent=0, duration=None, width=None, height=None):
        if width is None:
            width = self.getWindowWidth()
        if height is None:
            height = self.getWindowHeight()
        self.logger.info("Swipe up %s%% from the bottom. %s%% away from the bottom." % (move_offset_percent, bottom_offset_percent))
        self.swipe(width / 2, height - height / 100.0 * bottom_offset_percent, width / 2, height - height / 100.0 * bottom_offset_percent - height / 100.0 * move_offset_percent, duration, width, height)
        return self

    def swipeUpFromBottomToTop(self, top_offset_percent=0, bottom_offset_percent=0, duration=None, width=None, height=None):
        if width is None:
            width = self.getWindowWidth()
        if height is None:
            height = self.getWindowHeight()
        self.logger.info("Swipe up from the bottom to top. %s%% away from the top to %s%% away from the bottom." % (top_offset_percent, bottom_offset_percent))
        self.swipe(width / 2, height - height / 100.0 * bottom_offset_percent, width / 2, height / 100.0 * top_offset_percent, duration, width, height)
        return self

    def swipeUpFromMid(self, move_offset_percent=20, mid_offset_percent=0, duration=None, width=None, height=None):
        if width is None:
            width = self.getWindowWidth()
        if height is None:
            height = self.getWindowHeight()
        self.logger.info("Swipe up %s%% from the mid. %s%% away from the mid." % (move_offset_percent, mid_offset_percent))
        self.swipe(width / 2, height / 2 - height / 100.0 * mid_offset_percent, width / 2, height / 2 - height / 100.0 * mid_offset_percent - height / 100.0 * move_offset_percent, duration, width, height)
        return self

    def swipeLeftFromRight(self, move_offset_percent=20, right_offset_percent=0, duration=None, width=None, height=None):
        self.logger.info("Swipe left %s%% from the right. %s%% away from the right." % (move_offset_percent, right_offset_percent))
        if width is None:
            width = self.getWindowWidth()
        if height is None:
            height = self.getWindowHeight()
        self.swipe(width - width / 100.0 * right_offset_percent, height / 2, width - width / 100.0 * right_offset_percent - width / 100.0 * move_offset_percent, height / 2, duration, width, height)
        return self

    def swipeLeftFromMid(self, move_offset_percent=20, mid_offset_percent=0, duration=None, width=None, height=None):
        self.logger.info("Swipe left %s%% from the mid. %s%% away from the mid." % (move_offset_percent, mid_offset_percent))
        if width is None:
            width = self.getWindowWidth()
        if height is None:
            height = self.getWindowHeight()
        self.swipe(width / 2 - width / 100.0 * mid_offset_percent, height / 2, width / 2 - width / 100.0 * mid_offset_percent - width / 100.0 * move_offset_percent, height / 2, duration, width, height)
        return self

    def swipeRightFromLeft(self, move_offset_percent=20, left_offset_percent=0, duration=None, width=None, height=None):
        self.logger.info("Swipe right %s%% from the left. %s%% away from the left." % (move_offset_percent, left_offset_percent))
        if width is None:
            width = self.getWindowWidth()
        if height is None:
            height = self.getWindowHeight()
        self.swipe(width / 100.0 * left_offset_percent, height / 2, width / 100.0 * move_offset_percent, height / 2, duration, width, height)
        return self

    def swipeRightFromMid(self, move_offset_percent=20, mid_offset_percent=0, duration=None, width=None, height=None):
        self.logger.info("Swipe right %s%% from the mid. %s%% away from the mid." % (move_offset_percent, mid_offset_percent))
        if width is None:
            width = self.getWindowWidth()
        if height is None:
            height = self.getWindowHeight()
        self.swipe(width / 2 + width / 100.0 * mid_offset_percent, height / 2, width / 2 + width / 100.0 * mid_offset_percent + width / 100.0 * move_offset_percent, height / 2, duration, width, height)
        return self

    # def swipeDownFromTop(self, move_offset=200, top_offset=0, duration=None, width=None, height=None):
    #     if width is None:
    #         width = self.getWindowWidth()
    #     if height is None:
    #         height = self.getWindowHeight()
    #     self.logger.info("Swipe down %s from the top. %s away from the top" % (move_offset, top_offset))
    #     self.swipe(width / 2, top_offset, width / 2, top_offset + move_offset, duration, width, height)
    #     return self
    #
    # def swipeDownFromTopToBottom(self, top_offset=0, bottom_offset=0, duration=None, width=None, height=None):
    #     if width is None:
    #         width = self.getWindowWidth()
    #     if height is None:
    #         height = self.getWindowHeight()
    #     self.logger.info("Swipe down from the top to bottom. %s away from the top to %s away from the bottom." % (top_offset, bottom_offset))
    #     self.swipe(width / 2, top_offset, width / 2, height - bottom_offset, duration, width, height)
    #     return self
    #
    # def swipeDownFromMid(self, move_offset=200, mid_offset=0, duration=None, width=None, height=None):
    #     if width is None:
    #         width = self.getWindowWidth()
    #     if height is None:
    #         height = self.getWindowHeight()
    #     self.logger.info("Swipe down %s from the mid. %s away from the mid." % (move_offset, mid_offset))
    #     self.swipe(width / 2, height / 2 + mid_offset, width / 2, height / 2 + mid_offset + move_offset, duration, width, height)
    #     return self
    #
    # def swipeUpFromBottom(self, move_offset=200, bottom_offset=0, duration=None, width=None, height=None):
    #     if width is None:
    #         width = self.getWindowWidth()
    #     if height is None:
    #         height = self.getWindowHeight()
    #     self.logger.info("Swipe up %s from the bottom. %s away from the bottom." % (move_offset, bottom_offset))
    #     self.swipe(width / 2, height - bottom_offset, width / 2, height - bottom_offset - move_offset, duration, width, height)
    #     return self
    #
    # def swipeUpFromBottomToTop(self, top_offset=0, bottom_offset=0, duration=None, width=None, height=None):
    #     if width is None:
    #         width = self.getWindowWidth()
    #     if height is None:
    #         height = self.getWindowHeight()
    #     self.logger.info("Swipe up from the bottom to top. %s away from the top to %s away from the bottom." % (top_offset, bottom_offset))
    #     self.swipe(width / 2, height - bottom_offset, width / 2, top_offset, duration, width, height)
    #     return self
    #
    # def swipeUpFromMid(self, move_offset=200, mid_offset=0, duration=None, width=None, height=None):
    #     if width is None:
    #         width = self.getWindowWidth()
    #     if height is None:
    #         height = self.getWindowHeight()
    #     self.logger.info("Swipe up %s from the mid. %s away from the mid." % (move_offset, mid_offset))
    #     self.swipe(width / 2, height / 2 - mid_offset, width / 2, height / 2 - mid_offset - move_offset, duration, width, height)
    #     return self
    #
    # def swipeLeftFromRight(self, move_offset=200, right_offset=0, duration=None, width=None, height=None):
    #     self.logger.info("Swipe left %s from the right. %s away from the right." % (move_offset, right_offset))
    #     if width is None:
    #         width = self.getWindowWidth()
    #     if height is None:
    #         height = self.getWindowHeight()
    #     self.swipe(width - right_offset, height / 2, width - right_offset - move_offset, height / 2, duration, width, height)
    #     return self
    #
    # def swipeLeftFromMid(self, move_offset=150, mid_offset=0, duration=None, width=None, height=None):
    #     self.logger.info("Swipe left %s from the mid. %s away from the mid." % (move_offset, mid_offset))
    #     if width is None:
    #         width = self.getWindowWidth()
    #     if height is None:
    #         height = self.getWindowHeight()
    #     self.swipe(width / 2 - mid_offset, height / 2, width / 2 - mid_offset - move_offset, height / 2, duration, width, height)
    #     return self
    #
    # def swipeRightFromLeft(self, move_offset=200, left_offset=0, duration=None, width=None, height=None):
    #     self.logger.info("Swipe right %s from the left. %s away from the left." % (move_offset, left_offset))
    #     if width is None:
    #         width = self.getWindowWidth()
    #     if height is None:
    #         height = self.getWindowHeight()
    #     self.swipe(left_offset, height / 2, move_offset, height / 2, duration, width, height)
    #     return self
    #
    # def swipeRightFromMid(self, move_offset=200, mid_offset=0, duration=None, width=None, height=None):
    #     self.logger.info("Swipe right %s from the mid. %s away from the mid." % (move_offset, mid_offset))
    #     if width is None:
    #         width = self.getWindowWidth()
    #     if height is None:
    #         height = self.getWindowHeight()
    #     self.swipe(width / 2 + mid_offset, height / 2, width / 2 + mid_offset + move_offset, height / 2, duration, width, height)
    #     return self

    def openUrl(self, url):
        self.logger.info("Navigate to [" + url + "].")
        self._driver.get(url)

    def getElementWidth(self, item=None, element_name=None):
        element_name = self.getelement_nameFrom(element_name)
        return int(self._getElementObjectFromCurrentOrSearch(element_name, item).size["width"])

    def getElementWidthHeight(self, item=None, element_name=None):
        element_name = self.getelement_nameFrom(element_name)
        return int(self._getElementObjectFromCurrentOrSearch(element_name, item).size["height"])

    def getElemenX(self, item=None, element_name=None):
        element_name = self.getelement_nameFrom(element_name)
        return self._getElementObjectFromCurrentOrSearch(element_name, item).location["x"]

    def getElementY(self, item=None, element_name=None):
        element_name = self.getelement_nameFrom(element_name)
        return self._getElementObjectFromCurrentOrSearch(element_name, item).location["y"]

    def getWindowWidth(self):
        width = self._driver.get_window_size()['width']
        return width

    def getWindowHeight(self):
        height = self._driver.get_window_size()['height']
        return height