# coding: utf-8
import os
import re
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import Decorator
from UiBaseFwk import UiBaseFwk


class UiBaseWebDriverFwk(UiBaseFwk):
    def __init__(self, Init):
        UiBaseFwk.__init__(self, Init)
        if 2 == 1:
            self._driver = webdriver.Remote("")
        # self.Swipe = self._Swipe(self)

    def getDriverOnly(self):
        return self._driver

    def tap(self, left_offset=0, right_offset=0, up_offset=0, down_offset=0, duration=100, idx_or_match=None, element_name=None):
        xy = self.getElementCenterLocation(left_offset, right_offset, up_offset, down_offset, idx_or_match, element_name)
        self._driver.tap([(xy['x'], xy['y'])], duration)
        return self

    @Decorator.handle_action
    def click(self, idx_or_match=None, element_name=None):
        if self.getCurrentElementObject().is_enabled() is True:
            self.getCurrentElementObject().click()
        else:
            self.logger.error("The element [" + element_name + "] on the screen [" + str(self.CurrentElement.page_name) + "] is not enabled.")
        return self

    # def click1(self, idx_or_match=None, element_name=None):
    #     try:
    #         element = self._getCurrentElementObjectOrSearch(idx_or_match, element_name)
    #         element_name = self._getCurrentElementNameWhenNone(element_name)
    #         self.logger.info("Click element [" + element_name + "] on the screen [" + str(self.CurrentElement.page_name) + "].")
    #         if element.is_enabled() is True:
    #             element.click()
    #         else:
    #             self.logger.info("The element [" + element_name + "] on the screen [" + str(self.CurrentElement.page_name) + "] is not enabled.")
    #     except NoSuchElementException as e:
    #         self.logger.error(e)
    #         raise Exception(
    #             "Failed to click element [" + element_name + "] on the screen [" + str(self.CurrentElement.page_name) + "].")
    #     return self

    def setValue(self, value, idx_or_match=None, element_name=None):
        try:
            element_name = self._getCurrentElementNameWhenNone(element_name)
            element = self._getCurrentElementObjectOrSearch(idx_or_match, element_name)
            self.logger.info("Set the value of element [" + element_name + "] to [" + value + "].")
            self._driver.set_value(element, value)
        except Exception as e:
            self.logger.error("Failed to set the value of element [" + element_name + "] to [" + value + "].")
            raise Exception("Failed to set the value of element [" + element_name + "] to [" + value + "].")
        return self

    def setValueBySendKeys(self, value, idx_or_match=None, element_name=None):
        try:
            element_name = self._getCurrentElementNameWhenNone(element_name)
            element = self._getCurrentElementObjectOrSearch(idx_or_match, element_name)
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
        element = self._getCurrentElementObjectOrSearch(idx_or_match, element_name)
        return_value = ""
        if self.isVisible(idx_or_match, element_name):
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

    def _getXpathJoin(self, locator_value, value_type):
        matcher_array = re.findall(r'\+\+[^\-,+]*|--[^\-,+]*', locator_value)
        t = "//*["
        for index in range(len(matcher_array)):
            if index != 0 and index != len(matcher_array):
                t += " and "
            if matcher_array[index].startswith(self.Match.INCLUDE):
                t += "contains(" + value_type + ", '" + matcher_array[index].replace(self.Match.INCLUDE, "") + "')"
            else:
                t += "not(contains(" + value_type + ", '" + matcher_array[index].replace(self.Match.EXCLUDE, "") + "'))"
        t += "]"
        return t

    def _changeCutomizedToOriginal(self, locator_type, locator_value):
        if locator_type == self.LocatorType.TEXT or locator_type == self.LocatorType.VALUE or locator_type == self.LocatorType.CONTENT_DESC or locator_type == self.LocatorType.RESOURCE_ID or locator_type == self.LocatorType.CLASS or locator_type == self.LocatorType.TYPE:
            if self.Init.testType.lower() == self.Init.TestType.IOS.lower():
                if "@text" in locator_value:
                    locator_type = self.LocatorType.XPATH
                    locator_value = locator_value.replace("@text", "@value")
                elif ("(@" not in locator_value) and ("[@" not in locator_value):
                    if self.Match.INCLUDE in locator_value or self.Match.EXCLUDE in locator_value or self.Match.MATCH in locator_value:

                        if self.Match.MATCH in locator_value:
                            locator_value = locator_value.replace(self.Match.MATCH, "")
                        if not locator_value.startswith(self.Match.INCLUDE) and not locator_value.startswith(self.Match.EXCLUDE):
                            locator_value = self.Match.INCLUDE + locator_value
                        locator_value = self._getXpathJoin(locator_value, "@" + self._transformLocatorTypeToXpathStyle(locator_type))
                        locator_type = self.LocatorType.XPATH  # to avoid '//*[contains(@xpath, \\'AppImprovement\\')]', this change must be put here
                    else:
                        locator_type = "name"
            elif self.Init.testType.lower() == self.Init.TestType.ANDROID.lower():
                if "@name" in locator_value:
                    locator_value = locator_value.replace("@name", "@text")
                elif ("(@" not in locator_value) and ("[@" not in locator_value):
                    locator_type = self.LocatorType.XPATH
                    if self.Match.INCLUDE in locator_value or self.Match.EXCLUDE in locator_value or self.Match.MATCH in locator_value:
                        if self.Match.MATCH in locator_value:
                            locator_value = locator_value.replace(self.Match.MATCH, "")
                        if not locator_value.startswith(self.Match.INCLUDE) and not locator_value.startswith(self.Match.EXCLUDE):
                            locator_value = self.Match.INCLUDE + locator_value
                        locator_value = self._getXpathJoin(locator_value, "@" + self._transformLocatorTypeToXpathStyle(locator_type))
                        locator_type = self.LocatorType.XPATH
                    else:
                        locator_value = "//*[@text = '%s']" % locator_value
                        # if locator_value is chinese. str(locator_value)  => UnicodeEncodeError: 'ascii' codec can't encode characters in position 3-6: ordinal not in range(128)
                        # locator_value = "//*[@text = '%s']" % str(locator_value)
        return {self.Locator.TYPE: locator_type, self.Locator.VALUE: locator_value}

    # "//*[@text = 'HP Supplies Shopping']" "//*[contains(@text, 'HP Supplies Shopping')]"  "//*[contains(@text, 'HP Supplies Shopping') and not(contains(@text, 'xxxxxx'))]"

    def _findElementByLocatorsList(self, element_name, locatorsList, findOneOrCollection=None):
        ori_element_name = element_name
        list_for_log = []
        for locatorList in locatorsList:
            locator_type = self._getElementType(locatorList)
            locator_value = self._getElementValue(locatorList)
            if locator_value.strip() == "":
                continue
            locator_index = self._getElementIndex(locatorList)
            try:
                dict_type_value = self._changeCutomizedToOriginal(locator_type, locator_value)
                locator_type = dict_type_value[self.Locator.TYPE]
                locator_value = dict_type_value[self.Locator.VALUE]
                self.setCurrentElementIndex(locator_index)

                list_for_log.append({self.Locator.TYPE: locator_type, self.Locator.VALUE: locator_value, self.Locator.INDEX: locator_index, "element_name": element_name})

                if locator_type == self.LocatorType.ACCESSIBILITY_ID:
                    if findOneOrCollection == "findElements":
                        self.setCurrentElementCollectionName(element_name)
                        self.setCurrentElementCollectionIndex(locator_index)
                        self.setCurrentElementCollectionObject(self._driver.find_elements_by_accessibility_id(locator_value))
                        return self.getCurrentElementCollectionObject()
                    elif locator_index == 1:
                        self.setCurrentElementObject(self._driver.find_element_by_accessibility_id(locator_value))
                    else:
                        self.setCurrentElementObject(
                            self._driver.find_elements_by_accessibility_id(locator_value)[locator_index - 1])
                else:
                    if findOneOrCollection == "findElements":
                        self.setCurrentElementCollectionName(element_name)
                        self.setCurrentElementCollectionIndex(locator_index)
                        self.setCurrentElementCollectionObject(self._driver.find_elements(locator_type, locator_value))
                        return self.getCurrentElementCollectionObject()
                    elif locator_index == 1:
                        self.setCurrentElementObject(self._driver.find_element(locator_type, locator_value))
                    else:
                        self.setCurrentElementObject(
                            self._driver.find_elements(locator_type, locator_value)[locator_index - 1])
            except Exception as e:
                # traceback.print_exc()
                # print e.__str__()
                continue
            return self.getCurrentElementObject()
        for s in list_for_log:
            self.Init.logger.info(s)
        if findOneOrCollection == "findElements":  # When <id/xpath... index="0">android:id/checkbox</id>
            raise Exception("Failed to find all of the element [" + str(ori_element_name) + "] on the screen [" + str(
                self.getCurrentPageName()) + "].")
        elif locator_index == 1:  # When <id/xpath...>android:id/checkbox</id>
            raise Exception("Failed to find the element [" + str(ori_element_name) + "] on the screen [" + str(
                self.getCurrentPageName()) + "].")
        else:  # When <id/xpath... index="1/2/3.....">android:id/checkbox</id>
            raise Exception("Failed to find the element [" + str(ori_element_name) + "] with index [" + str(
                locator_index + 1) + "] on the screen [" + str(self.getCurrentPageName()) + "].")

    def _findElement(self, element_name, findOneOrCollection=None):
        if self.CurrentElement.name == element_name and self.CurrentElement.list_locators is not None:
            list_locator = self.CurrentElement.list_locators  # for
        else:
            list_locator = self._getElementLocatorsDictList(element_name)
            if list_locator[0][self.Locator.REF] is not None:
                ref_type = list_locator[0][self.Locator.REF].split(":")[0]
                ref_name = list_locator[0][self.Locator.REF].split(":")[1]
                #  self.RefElement.name = ref_name
                ref_locatorsList = self._getElementLocatorsDictList(ref_name)
                if self.Ref.NEARBY.lower() == ref_type.lower():
                    list_locator = self._getLocatorListByNearbyUniqueElement(element_name, list_locator, ref_locatorsList)
                else:
                    pass
        return self._findElementByLocatorsList(element_name, list_locator, findOneOrCollection)

    # def getElementsSize(self, name):
    #     return len(self.getElements(name))

    def getMatchedElements(self, match=None, element_name=None):
        return self._findElements(element_name)

    def getMatchedElement(self, idx_or_match=None, element_name=None):
        if idx_or_match is None:
            return self._findElement(element_name)
        elements = self._findElements(element_name)
        if idx_or_match == None:
            if str(type(elements)) == "<class \'appium.webdriver.webelement.WebElement\'>":  # accessibility_id    webelement has no len(x)
                return elements
            elif len(elements) == 0:
                raise IndexError("Cannot find the element [ " + str(
                    element_name) + "] on the screen [" + str(self.CurrentElement.page_name) + "].")
            elif len(elements) != 1:
                raise IndexError("There are multiple matched elements that found, please check element [" + str(element_name) + "] on the screen [" + str(self.CurrentElement.page_name) + "].")
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
            index = idx_or_match - 1
        return index

    def __getScreenShot(self, name, Result):
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

    def _dragByNative(self, origin_el, destination_el):
        self._driver.drag_and_drop(origin_el, destination_el)
        return self

    def openUrl(self, url):
        self.logger.info("Navigate to [" + url + "].")
        self._driver.get(url)

    def getElementWidth(self, item=None, element_name=None):
        element_name = self._getCurrentElementNameWhenNone(element_name)
        return int(self._getCurrentElementObjectOrSearch(item, element_name).size["width"])

    def getElementHeight(self, item=None, element_name=None):
        element_name = self._getCurrentElementNameWhenNone(element_name)
        return int(self._getCurrentElementObjectOrSearch(item, element_name).size["height"])

    def getElemenX(self, item=None, element_name=None):
        element_name = self._getCurrentElementNameWhenNone(element_name)
        return self._getCurrentElementObjectOrSearch(item, element_name).location["x"]

    def getElementY(self, item=None, element_name=None):
        element_name = self._getCurrentElementNameWhenNone(element_name)
        return self._getCurrentElementObjectOrSearch(item, element_name).location["y"]

    def getWindowWidth(self):
        width = self._driver.get_window_size()['width']
        return width

    def getWindowHeight(self):
        height = self._driver.get_window_size()['height']
        return height

    def getWindowSize(self):
        size = self._driver.get_window_size()
        return {'width': size['width'], 'height': size['height']}

    def getElementCenterLocation(self, left_offset_percent=0, right_offset_percent=0, up_offset_percent=0, down_offset_percent=0, item=None, element_name=None):
        element = self._getCurrentElementObjectOrSearch(item, element_name)
        element_name = self._getCurrentElementNameWhenNone(element_name)
        t = element.size["width"]
        centerX = element.location["x"] + t / 2 - t / 2 * left_offset_percent / 100.0 + t / 2 * right_offset_percent / 100.0
        t = element.size["height"]
        centerY = element.location["y"] + t / 2 - t / 2 * up_offset_percent / 100.0 + t / 2 * down_offset_percent / 100.0
        return {'x': centerX, 'y': centerY}

    def getElementCenterX(self, left_offset_percent=0, right_offset_percent=0, item=None, element_name=None):
        return self.getElementCenterLocation(left_offset_percent, right_offset_percent, 0, 0, item, element_name)['x']

    def getElementCenterY(self, up_offset_percent=0, down_offset_percent=0, item=None, element_name=None):
        return self.getElementCenterLocation(0, 0, up_offset_percent, down_offset_percent, item, element_name)['y']
