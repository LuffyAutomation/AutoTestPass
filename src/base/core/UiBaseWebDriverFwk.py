from UiBaseFwk import UiBaseFwk
from src.base.core.InitFwk import InitFwk
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from appium import webdriver
import os


class UiBaseWebDriverFwk(UiBaseFwk):
    def __init__(self, Init):
        UiBaseFwk.__init__(self, Init)
        if 2 == 1:
            self._driver = webdriver.Remote("")

    def click(self, idx_or_match=None, element_name=None):
        try:
            element = self.getElementObjectFrom(idx_or_match, element_name)
            element_name = self.getElementNameFrom(element_name)
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
            element_name = self.getElementNameFrom(element_name)
            self.logger.info("Set the value of element [" + element_name + "] to [" + value + "].")
            element = self.getElementObjectFrom(idx_or_match, element_name)
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
        except NoSuchElementException as e:
            self.logger.error("Set the value of element [" + element_name + "] to [" + value + "] failed.")
            raise Exception("Set the value of element [" + element_name + "] to [" + value + "] failed.")
        return self

    def _getElementTagName(self, element):
        # get element tar name
        try:
            elementType = element.tag_name
            try:
                elementType += element.get_attribute("type")
            except NoSuchElementException as e:
                pass
            if elementType in "select":
                elementType = "select"
            elif elementType in "checkbox":
                elementType = "checkbox"
            elif elementType in "input":
                elementType = "input"
            else:
                elementType = "text"
            return elementType
        except Exception as e:
            #raise Exception("get element tag name failed.")
            return "text"

    def getValue(self, attribute_type=None, idx_or_match=None, element_name=None):
        element = self.getElementObjectFrom(element_name, idx_or_match)
        return_value = ""
        if self.isPresent(element_name, idx_or_match):
            if attribute_type is None:
                element_type = self._getElementTagName(element)
                if "input" in element_type:
                    return_value = element.get_attribute(self.AttributeType.VALUE)
                elif "text" in element_type:
                    return_value = element.text
                elif "checkbox" in element_type:
                    checkbox_class = element.get_attribute(self.AttributeType.CLASS)
                    if "checked" in checkbox_class:
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
        locator_type = None
        locator_value = None
        locatorsDictList = self._getElementLocatorsList(element_name)
        if locator_type == self.LocatorType.ACCESSIBILITY_ID:
            return self._driver.find_elements_by_accessibility_id(locator_value)
        else:
            return self._driver.find_elements(locator_type, locator_value)

    def _findElement(self, element_name):
        locatorsList = self._getElementLocatorsList(element_name)

        for locatorList in locatorsList:
            locator_type = self._getElementType(locatorList)
            locator_value = self._getElementValue(locatorList)
            locator_value = self._getLocatorValueByLocalString(element_name, locator_value)
            try:
                if locator_type == self.LocatorType.ACCESSIBILITY_ID:
                    self.setCurrentElementObject(self._driver.find_element_by_accessibility_id(locator_value))
                else:
                    self.setCurrentElementObject(self._driver.find_element(locator_type, locator_value))
            except Exception as e:
                # traceback.print_exc()
                # print e.__str__()
                continue
            return self.getCurrentElementObject()
        #return None
        raise Exception("Failed to find element [" + str(
            element_name) + "] on [" + str(self.getCurrentPage()) + "] page.")

    def getElementsSize(self, element_name):
        return len(self.getElements(element_name))

    def getMatchedElement(self, idx_or_match=None, element_name=None):
        if idx_or_match is None:
            return self._findElement(element_name)
        elements = self._findElements(element_name)
        if idx_or_match == None:
            if str(type(elements)) == "<class \'appium.webdriver.webelement.WebElement\'>": #accessibility_id    webelement no len(x)
                return elements
            elif len(elements) == 0:
                raise IndexError("Cannot find element [ " + str(
                    element_name) + "] on [" + str(self._currentPage) + "] page.")
            elif len(elements)!=1:
                raise IndexError("There are multiple matched elements that found, please check element [" + str(element_name) +"] on ["+str(self._currentPage) + "] page.")
            else:
                return elements[0]
        else:
            index = self.__getMatchedIndex(elements, idx_or_match)
            return elements[index]

    def __getMatchedIndex(self, elements, idx_or_match, attribute="text"):
        if type(idx_or_match) == type(1):
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
            if self._drive is not None:
                self._driver.quit()
        except Exception as e:
            pass