
from src.base.core.InitializeFramework import InitializeFramework
from selenium.common.exceptions import NoSuchElementException
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from abc import abstractmethod
from appium import webdriver
import os
import traceback

class UIFramework(InitializeFramework):
    class StringConverter:
        VALUE_PLACEHOLDER = 'VALUE_PLACEHOLDER'
        MARK_DYNAMIC_VALUE = ' : '
    class SwipeTo:
        LEFT = "left"
        LEFT_SIDE = "leftSide"
        RIGHT = "right"
        RIGHT_SIDE = "rightSide"
        UP = "up"
        TOP = "top"
        DOWN = "down"
        BOTTOM = "bottom"

    class _LogHead:
        VERIFY = "Verify"
        WAITINGFOR = "Waiting for"

    class LocatorType:
        ID = "id"
        XPATH = "xpath"
        LINK_TEXT = "link_text"
        PARTIAL_LINK_TEXT = "partial_link_text"
        NAME = "name"  # text
        ACCESSIBILITY_ID = "accessibility_id"  #1. content-desc 2. equal to name in some cases. But name has been depreated in appium 1.6
        TAG_NAME = "tag_name"
        CLASS_NAME = "class_name"
        CSS_SELECTOR = "css_selector"

    class AttributeType:
        NAME = "name"
        CLASS = "class"
        VALUE = "value"

    def __init__(self):
        InitializeFramework.__init__(self)
        self._driver = None
        if 2 == 1:
            self._driver = webdriver.Remote("")

    def wait(self, time):
        try:
            self.logger.info("Wait " + time + "s.")
            self.UtilTime.sleep(time)
        except Exception as e:
            pass
        return self

    def getUiMap(self, page):
        xpath = ".//page[@name='"+page+"']/element"
        return self.getUiMapByXpath(xpath)

    def getUiMapOfSubPage(self, page, subPage):
        xpath = ".//page[@name='"+page+"']/page[@name='"+subPage+"']/element"
        return self.getUiMapByXpath(xpath)

    def getUiMapByXpath(self, xpath):
        list = self.UtilXml.getElements(self._root, xpath)
        currentElements = {}
        for index in range(len(list)):
            attributes = self.UtilXml.getAttribute(list[index])
            children = self.UtilXml.getChildren(list[index])
            name = attributes.get("name")
            attributes["locators"] = children
            currentElements[name] = attributes
        if len(list) == len(currentElements):
            return currentElements
        else:
            raise Exception("There are duplicated pages exist. [" + xpath + "].")

    def getUiMapRoot(self):
        return self._root

    def _getElementType(self, element_locators_list):
        return element_locators_list[0]

    def _getElementValue(self, element_locators_list):
        return element_locators_list[1]

    def getElementNameFrom(self, element_name=None):
        if element_name == None:
            element_name = self.getCurrentElementName()
        return element_name

    def getElementObjectFrom(self, idx_or_match=None, element_name=None):
        if self.getCurrentElementObject() is not None:
            return self.getCurrentElementObject()
        self.setCurrentElementObject(self.getMatchedElement(idx_or_match, self.getCurrentElementName()))
        return self.getCurrentElementObject()

    def waitForShown(self, time_out=None, idx_or_match=None, element_name=None, verify_shown=True, log_head=None):
        element_name = self.getElementNameFrom(element_name)
        if log_head == None: log_head = self._LogHead.WAITINGFOR
        if time_out == None:
            try:
                time_out = float(self._elementTimeOut)
            except TimeoutException:
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
            # WebDriverWait(self._driver, time_out,).until(
            #     lambda show:
            #         self.isPresent(idx_or_match, element_name) if verify_shownOrNot else not self.isPresent(idx_or_match, element_name)
            # )
            # HandleWaitEvent(time_out).until(
            #     lambda x: self.isPresent(idx_or_match, element_name) if verify_shownOrNot else not self.isPresent(idx_or_match, element_name)
            # )
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

    def __getLocalString(self, element_name):
        try:
            ele = self.UtilXml.getElement(self._rootLocalXml, ".//page[@name='"+self.getCurrentPage()+"']/element[@name='"+element_name+"']")
            return self.UtilXml.getText(ele).strip()
        except:
            raise Exception("Failed to get local string, please check element [" + str(element_name) + "] on [" +str(self.getCurrentPage()) + "] page.")

    def _getElementLocatorsList(self, element_name):
        dynamic_string = None
        if self.StringConverter.MARK_DYNAMIC_VALUE in element_name:
            dynamic_string = element_name.split(self.StringConverter.MARK_DYNAMIC_VALUE)[1]
            element_name = element_name.split(self.StringConverter.MARK_DYNAMIC_VALUE)[0]
        locators = self._currentUiMap.get(element_name)['locators']
        list = []
        for locator in locators:
            locator_type = self.UtilXml.getTagName(locator)
            locator_type = self.__get_sys_locator_type(locator_type)
            locator_value = self.UtilXml.getText(locator).strip()
            if dynamic_string is not None and self.StringConverter.VALUE_PLACEHOLDER in locator_value:
                locator_value = locator_value.replace(self.StringConverter.VALUE_PLACEHOLDER, dynamic_string)
            #self.logger.info("............Finding element [" + element_name + "] of page [" + str(self.getCurrentPage()) + "]. locator_type is [" + locator_type + "] locator_value is [" + locator_value + "].")
            list.append([locator_type, locator_value])
        if locators == None:
            raise Exception("Can not find element [" + element_name + "] on [" + str(self._currentPage) + "] page.")
        return list

    def __get_sys_locator_type(self, locator_type):
        if locator_type == self.LocatorType.ID:
            locator_type = By.ID
        elif locator_type == self.LocatorType.NAME:
            locator_type = By.NAME # it is deprecated in 1.5
        elif locator_type == self.LocatorType.XPATH:
            locator_type = By.XPATH
        elif locator_type == self.LocatorType.PARTIAL_LINK_TEXT:
            locator_type = By.PARTIAL_LINK_TEXT
        elif locator_type == self.LocatorType.TAG_NAME:
            locator_type = By.TAG_NAME
        elif locator_type == self.LocatorType.CLASS_NAME:
            locator_type = By.CLASS_NAME
        elif locator_type == self.LocatorType.ACCESSIBILITY_ID:
            locator_type = self.LocatorType.ACCESSIBILITY_ID
        else:  # locator_type="css selector"
            locator_type = By.CSS_SELECTOR
        return locator_type

    def __getReplacedLocatorByLocalString(self, locator_value, localString):
        objlocalString = ""
        tList = ["@ text = '", "@text = '", "@text= '", "@text='", "@ text= '", "@ text='"]# // android.widget.TextView[ @ text = 'Choose a mail provider']
        for t in tList:
            if t in locator_value:
                objlocalString = locator_value.split(t)[1].split("']")[0]
                return locator_value.replace(objlocalString, localString)
        tList = ["@ text, '", "@ text,'", "@text,'", "@text, '"]  #// android.widget.TextView[contains( @ text, 'VALUE_PLACEHOLDER')]
        for t in tList:
            if t in locator_value:
                objlocalString = locator_value.split(t)[1].split("')]")[0]
                return locator_value.replace(objlocalString, localString)
        return localString

    def __getLocatorValueByLocalString(self, element_name, locator_value):
        if element_name.endswith("_") and self.getMobileLanguageRegion() != self.Language.en_US:
            localString = self.__getLocalString(element_name)
            return self.__getReplacedLocatorByLocalString(locator_value, localString)
        return locator_value

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
            locator_value = self.__getLocatorValueByLocalString(element_name, locator_value)
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

    def forTestPurpose(self):
        pass

    def _getElements(self, element_name):
        return self._findElements(element_name)

    def _getElement(self, element_name):
        return self._findElement(element_name)

    def getElementsSize(self, element_name):
        return len(self.getElements(element_name))

    def getMatchedElement(self, idx_or_match=None, element_name=None):
        if idx_or_match is None:
            return self._getElement(element_name)
        elements = self._getElements(element_name)
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

    def relocateByText(self, dynamicValue, element_name=None):
        element_name = self.getElementNameFrom(element_name)
        self._currentElementName = element_name + self.StringConverter.MARK_DYNAMIC_VALUE + dynamicValue
        return self

    def updateCurrentElementStatus(self, element_name, uiMap, currentPage):
        if self._currentElementName != element_name:
            self._currentElementObject = None
        self._currentUiMap = uiMap
        self._currentPage = currentPage
        self._currentElementName = element_name
        return self

    #some elements' locator may change after they appear. So need to clear the found ele and re-find.
    def clearForRefinding(self):
        self.urrentElementObject()

    def setCurrentElementName(self, element_name):
        self._currentElementName = element_name

    def getCurrentElementName(self):
        return self._currentElementName

    def setCurrentPage(self, page):
        self._currentPage = page

    def getCurrentPage(self):
        return self._currentPage

    def setCurrentElementObject(self, element=None):
        self._currentElementObject = element

    def getCurrentElementObject(self):
        return self._currentElementObject

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
            self._driver.quit()
        except Exception as e:
            pass