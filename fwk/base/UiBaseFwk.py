# coding: utf-8
import os
import re
from selenium.webdriver.common.by import By
from fwk.utils.exceller.Exceller import Exceller
from fwk.other.RunTimeConf import RunTimeConf
from fwk.utils.utilTime.UtilWaitEvent import UtilWaitEvent


class UiBaseFwk(object):
    class StringConverter:
        VALUE_PLACEHOLDER = 'VALUE_PLACEHOLDER'
        MARK_DYNAMIC_VALUE = ' : '

    class Match:
        MATCH = ".*"
        INCLUDE = "++"
        EXCLUDE = "--"

    class Language:
        en_US = "en_US"
        list = (en_US)
        def __init__(self, language):
            if language.lower() == "en" or language.lower() == self.en_US.lower():
                return self.en_US

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

    class Locator:
        TYPE = "type"
        VALUE = "value"
        INDEX = "index"
        REF = "ref"

    class Ref:
        NEARBY = "Nearby"
        LEFT = "Left"
        LOWER = "Lower"
        UPPER = "Upper"
        RIGHT = "Right"

    class LocatorType:
        ID = "id"  # all
        XPATH = "xpath"  # all
        LINK_TEXT = "link_text"
        PARTIAL_LINK_TEXT = "partial_link_text"
        NAME = "name"  # text, but name has been depreated in appium 1.6 for Android ??  But it works in IOS.
        ACCESSIBILITY_ID = "accessibility_id"  #1. equals to content-desc 2. equal to name in some cases. But name has been depreated in appium 1.6
        TAG_NAME = "tag_name"
        CLASS_NAME = "class_name"  # web
        CSS_SELECTOR = "css_selector"
        CONTENT_DESC = "content-desc"  # android, used in uimap
        CONTENT_DESC1 = "content_desc"  # android, used for xpath
        RESOURCE_ID = "resource-id"  # android, used in xpath
        RESOURCE_ID1 = "resource_id"  # android, used in uimap
        CLASS = "class"  # android
        TYPE = "type"  # ios

        TEXT = "text"  # customized, it is slower than other types
        VALUE = "value"  # customized, it is slower than other types

    class AttributeType:
        NAME = "name"
        CLASS = "class"
        VALUE = "value"
        CHECKED = 'checked'

    class ElementStruct:
        page_name = None
        page_uiMap = None
        name = None
        object = None
        index = None
        list_locators = None

    def __init__(self, Init):
        self.Init = Init
        self.logger = self.Init.logger
        self.UtilWaitEvent = UtilWaitEvent
        self.UtilXml = self.Init.UtilXml
        self.UtilTime = self.Init.UtilTime
        self.UtilFile = self.Init.UtilFile
        self.UtilFolder = self.Init.UtilFolder
        self.UtilString = self.Init.UtilString
        self.UtilConsole = self.Init.UtilConsole
        self.TestType = self.Init.TestType
        self.testType = self.Init.testType
        self._xmlRoot = None
        self._xmlRootLocalXml = None

        self.CurrentElement = self.ElementStruct()
        self.LastElement = self.ElementStruct()
        self.CurrentElementCollection = self.ElementStruct()
        self.RefElement = self.ElementStruct()
        # self._lastElementName = None
        # self._lastElementObject = None

        # self._currentFunction = None

        # self._currentElementName = None
        # self._currentElementObject = None

        self._currentElementCollectionName = None
        self._currentElementCollectionObject = None

        self._currentPage = None
        self._currentUiMap = None
        self._elementTimeOut = None
        self._getCurrentTestArgs(self.testType)
        self.__getConfigurationParameters()
        self.RunTimeConf = RunTimeConf(self.Init.ConfigParser)
        self._driver = None

        self.path_file_xlsx_testData = ""
        self._DictTestData = None
        self._HasSearchedTestData = False

        self.hasGotDriver = False

    def __getConfObject(self, configFileName):
        return self.Init.ConfigParser.getConf(configFileName)

    def _getCurrentTestArgs(self, testType):
        try:
            # local pc /opt/devicepass/android/automation-workspace/1adaa521831046b985b39f5ea27b30b3/python-work-HC43YWW01974/projects/PrinterControl/data/Android/runTime.conf
            # both Android/ android are right. But in DP Android will fail.
            testType = testType.lower()
            self._path_file_runTimeConf = os.path.join(self.Init.path_folder_data, testType, 'runTime.conf')
        except:
            if testType is None:
                self.logger.error("failed to find [%s] from [%s]." % (self.Init._name_project, self.Init._path_file_mainConf))
        self.__RunTimeConfig = self.__getConfObject(self._path_file_runTimeConf)
        self.Init.ConfigParser.setRunTimeConfig(self.__RunTimeConfig)
        self._path_folder_uiMaps = os.path.join(self.Init.path_folder_data, testType, 'uiMaps')
        self._path_file_uiMap = os.path.join(self._path_folder_uiMaps, self.Init.ConfigParser.getRunTimeConfigArgsValue(self.Init.ConfigParser.TEST_UIMAP_FILENAME))
        self.language = self.Init.ConfigParser.getRunTimeConfigArgsValue(self.Init.ConfigParser.TEST_LANGUAGE)
        self._path_file_uiMap_localized = os.path.join(self._path_folder_uiMaps, self.language)
        if not self._path_file_uiMap_localized.lower().endswith(".xml"):
            self._path_file_uiMap_localized += ".xml"

    def getLanguage(self):
        return self.language

    def __getConfigurationParameters(self):
        self._xmlTree = self.UtilXml.getTree(self._path_file_uiMap)
        self._xmlRoot = self.UtilXml.getRootElement(self._xmlTree)
        self._elementTimeOut = self.Init.ConfigParser.getRunTimeConfigArgsValue(self.Init.ConfigParser.TEST_TIMEOUT_ELEMENT)

        self._xmlTree_localized = None
        self._xmlRoot_localized = None
        try:
            self._xmlTree_localized = self.UtilXml.getTree(self._path_file_uiMap_localized)
            self._xmlRoot_localized = self.UtilXml.getRootElement(self._xmlTree_localized)
        except:
            self.logger.warning("Please make sure if [%s] is existing. Or Please check if the [test.language=] is set correctly in runTime.conf." % (self._path_file_uiMap_localized))

    def __addLogForWaitEvent(self, method, log):
        if ". 0s elapsed" not in log:  # ignore this
            self.logger.info(log)
        return method()

    def waitUntil(self, method, error_message="Wait failed.", time_out=None, poll_frequency=2, log_prefix=None):
        if log_prefix is None:
            log_prefix = "Finding element [" + str(self.getCurrentElementName()) + "] of page [" + str(self.getCurrentPageName()) + "]."
        if time_out is None:
            try:
                time_out = float(self._elementTimeOut)
            except Exception:
                time_out = 60
        self.UtilWaitEvent(time_out, poll_frequency).until(
            lambda start_time: self.__addLogForWaitEvent(method, "......%s %ss elapsed. Timeout is %ss. Interval is %ss." % (log_prefix, start_time, time_out, poll_frequency)), error_message
        )

    def wait(self, time):
        try:
            # self.logger.info("Wait " + str(time) + "s.")
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
        list = self.UtilXml.getElements(self._xmlRoot, xpath)
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
            raise Exception("There are duplicated pages existing. [" + xpath + "].")

    def _getUiMapRoot(self):
        return self._xmlRoot

    # there are 3 same functions in AndroidFwk, IosFwk, WebFwk
    # def updateCurrentElementStatus(self, element_name, uiMap, page_name):
    #     if self.CurrentElement.name != element_name:
    #         self.LastElement.object = self.CurrentElement.object
    #         self.LastElement.page_uiMap = self.CurrentElement.page_uiMap
    #         self.LastElement.page_name = self.CurrentElement.page_name
    #         self.LastElement.list_locators = self.CurrentElement.list_locators
    #         self.CurrentElement.object = None
    #         self.CurrentElement.list_locators = None
    #     self.CurrentElement.page_uiMap = uiMap
    #     self.LastElement.name = self.CurrentElement.name
    #     self.CurrentElement.page_name = page_name
    #     self.CurrentElement.name = element_name
    #     return self

    # if define VALUE_PLACEHOLDER in uimap:
    # <element name="text_printerIp" page="page_home"><xpath>//android.widget.TextView[contains(@text,'VALUE_PLACEHOLDER')]</xpath></element>
    # you can find the element by  xxx.replacePlaceholder("10").click
    def replacePlaceholder(self, dynamic_value, element_name=None):
        element_name = self._getCurrentElementNameWhenNone(element_name)
        self.CurrentElement.name = element_name + self.StringConverter.MARK_DYNAMIC_VALUE + dynamic_value
        return self

    #some elements' status may change after they appear. So need to clear the found ele and re-find.
    def refreshMe(self):
        self.setCurrentElementObject(None)
        self.setCurrentElementCollectionObject(None)
        return self

    def setCurrentElementName(self, element_name):
        self.CurrentElement.name = element_name

    def getCurrentElementName(self):
        return self.CurrentElement.name

    def setCurrentElementObject(self, element=None):
        self.CurrentElement.object = element

    def setCurrentElementIndex(self, index=None):
        self.CurrentElement.index = index

    def getCurrentElementObject(self):
        return self.CurrentElement.object

    def getLastElementName(self):  # when using this kind of method  .swithToElement
        return self.LastElement.name

    def getLastElementObject(self):
        return self.LastElement.object

    def setLastElementObject(self, element=None):
        self.LastElement.object = element

    def setCurrentElementCollectionName(self, elementCollection_name):
        self.CurrentElementCollection.name = elementCollection_name

    def setCurrentElementCollectionIndex(self, elementCollection_index):
        self.CurrentElementCollection.index = elementCollection_index

    def getCurrentElementCollectionName(self):
        return self.CurrentElementCollection.name

    def setCurrentElementCollectionObject(self, element=None):
        self.CurrentElementCollection.object = element

    def getCurrentElementCollectionObject(self):
        return self.CurrentElementCollection.object

    def _setCurrentPageName(self, page_name):
        self.CurrentElement.page_name = page_name

    def getCurrentPageName(self):
        return self.CurrentElement.page_name

    def _getElementType(self, element_locators_list):
        return element_locators_list[self.Locator.TYPE]

    def _getElementValue(self, element_locators_list):
        return element_locators_list[self.Locator.VALUE]

    def _getElementIndex(self, element_locators_list):
        t = element_locators_list[self.Locator.INDEX]
        try:
            return int(t)
        except:
            return 1

    # for log
    def _getCurrentElementNameWhenNone(self, element_name=None):
        if element_name == None:
            element_name = self.getCurrentElementName()
        if type(element_name) is not str:  # ElementStruct
            return element_name.name
        return element_name

    def _getCurrentElementObjectOrSearch(self, idx_or_match=None, element_name=None):
        if element_name is not None:
            if type(element_name) is not str:  #  ElementStruct
                return element_name.object
            if self.CurrentElement.name == element_name and self.getCurrentElementObject() is not None:
                return self.CurrentElement.object
        elif self.getCurrentElementObject() is not None:
            return self.getCurrentElementObject()
        self.setCurrentElementObject(self.getMatchedElement(idx_or_match, self.getCurrentElementName()))
        return self.getCurrentElementObject()

    def _getLastElementObjectOrSearch(self, idx_or_match=None, element_name=None):
        if type(element_name) is not str:  # ElementStruct
            return element_name
        if self.getLastElementObject() is not None and self.LastElement.name == element_name:
            return self.getLastElementObject()
        self.setLastElementObject(self.getMatchedElement(idx_or_match, element_name))
        return self.getLastElementObject()

    def _getCurrentElementCollectionName(self, element_name=None):
        if element_name == None:
            element_name = self.getCurrentElementCollectionName()
        return element_name

    def _getElementCollectionObjectFromCurrentOrSearch(self, idx_or_match=None, element_name=None):
        if self.getCurrentElementCollectionObject() is not None:
            return self.getCurrentElementCollectionObject()
        self.setCurrentElementCollectionObject(self.getMatchedElements(idx_or_match, self.getCurrentElementName()))
        return self.getCurrentElementCollectionObject()

    def _getElementLocatorsDictList(self, element_name, WhichElement=None):
        dynamic_string = None
        ori_element_name = element_name
        if WhichElement is None:
            WhichElement = self.CurrentElement
        if self.StringConverter.MARK_DYNAMIC_VALUE in element_name:
            dynamic_string = element_name.split(self.StringConverter.MARK_DYNAMIC_VALUE)[1]
            element_name = element_name.split(self.StringConverter.MARK_DYNAMIC_VALUE)[0]
        uiMapByName = WhichElement.page_uiMap.get(element_name)
        locators = uiMapByName['locators']
        locator_ref = None
        try:
            locator_ref = uiMapByName[self.Locator.REF]
        except:
            pass
        list = []
        for locator in locators:
            locator_type = self.UtilXml.getTagName(locator)
            locator_type = self._get_native_locator_type(locator_type)
            locator_value = self.UtilXml.getText(locator).strip()
            locator_value = self._getLocatorValueByLocalString(element_name, locator_type, locator_value)
            global locator_index
            try:
                locator_index = self.UtilXml.getAttribute(locator)['index']
            except:
                locator_index = "1"
            if dynamic_string is not None and self.StringConverter.VALUE_PLACEHOLDER in locator_value:
                locator_value = locator_value.replace(self.StringConverter.VALUE_PLACEHOLDER, dynamic_string)
            #self.logger.info("............Finding element [" + name + "] of page [" + str(self.getCurrentPage()) + "]. locator_type is [" + locator_type + "] locator_value is [" + locator_value + "].")
            list.append({self.Locator.TYPE: locator_type, self.Locator.VALUE: locator_value, self.Locator.INDEX: locator_index, self.Locator.REF: locator_ref})
        if locators == None:
            raise Exception("Can not find element [" + ori_element_name + "] on page [" + str(self.CurrentElement.page_name) + "].")
        return list

    def _get_native_locator_type(self, locator_type):
        if locator_type == self.LocatorType.ID or locator_type == self.LocatorType.RESOURCE_ID or locator_type == self.LocatorType.RESOURCE_ID1:
            locator_type = By.ID
        elif locator_type == self.LocatorType.NAME:
            locator_type = By.NAME
        elif locator_type == self.LocatorType.XPATH:
            locator_type = By.XPATH
        elif locator_type == self.LocatorType.PARTIAL_LINK_TEXT:
            locator_type = By.PARTIAL_LINK_TEXT
        elif locator_type == self.LocatorType.TAG_NAME:
            locator_type = By.TAG_NAME
        elif locator_type == self.LocatorType.TEXT:
            locator_type = self.LocatorType.TEXT
        elif locator_type == self.LocatorType.CLASS_NAME:
            locator_type = By.CLASS_NAME
        elif locator_type == self.LocatorType.ACCESSIBILITY_ID:
            locator_type = self.LocatorType.ACCESSIBILITY_ID
        elif locator_type == self.LocatorType.CONTENT_DESC or locator_type == self.LocatorType.CONTENT_DESC1:
            locator_type = self.LocatorType.CONTENT_DESC
        else:  # locator_type="css selector"
            locator_type = By.CSS_SELECTOR
        return locator_type

    def __getReplacedLocatorByLocalString(self, locator_value, local_string):
        if self._hasXpathText(local_string):
            return local_string

        matcher_array = [locator_value]
        if "(@" in locator_value:
            matcher_array = re.findall("\'([^\"]*)\'\)\]", locator_value)
            if matcher_array.__len__() == 0:
                matcher_array = re.findall("\"([^\"]*)\"\)\]", locator_value)
                if matcher_array.__len__() == 0:
                    raise Exception("The xpath [" + locator_value + "] for element [" + str(self.getCurrentElementName()) + "] is unavailable.")
        elif "[@" in locator_value:
            matcher_array = re.findall("\'([^\"]*)\'\]", locator_value)
            if matcher_array.__len__() == 0:
                matcher_array = re.findall("\"([^\"]*)\"\]", locator_value)
                if matcher_array.__len__() == 0:
                    raise Exception("The xpath [" + locator_value + "] for element [" + str(self.getCurrentElementName()) + "] is unavailable.")
        locator_value = locator_value.replace(matcher_array[0], local_string)
        return locator_value

        # tList = ["@ text = '", "@text = '", "@text= '", "@text='", "@ text= '", "@ text='"]  # // android.widget.TextView[@ text = 'Choose a mail provider']
        # for t in tList:
        #     if t in locator_value:
        #         objlocalString = locator_value.split(t)[1].split("']")[0]
        #         return locator_value.replace(objlocalString, localString)
        # tList = ["@ text, '", "@ text,'", "@text,'", "@text, '"]  # // android.widget.TextView[contains(@text, 'VALUE_PLACEHOLDER')]
        # for t in tList:
        #     if t in locator_value:
        #         objlocalString = locator_value.split(t)[1].split("')]")[0]
        #         return locator_value.replace(objlocalString, localString)
        # return localString

    def _getLocalStringFromFile(self, element_name, locator_type):
        if self._xmlRoot_localized is None:
            return None
        try:
            t_page_name = self.getCurrentPageName()
            if "\\" in t_page_name:
                list_page_name = t_page_name.split("\\")
                t_page_name = list_page_name[0] + "']/page[@name='" + list_page_name[1]
            ele = self.UtilXml.getElement(self._xmlRoot_localized, ".//page[@name='" + t_page_name + "']/element[@name='" + element_name + "']/%s" % locator_type)
            # if ele is None:  # Maybe the locator_type from uiMap is unmatched with the corresponding one from localized uiMap.
            #     ele = self.UtilXml.getElement(self._xmlRoot_localized, ".//page[@name='" + self.getCurrentPageName() + "']/element[@name='" + element_name + "']/*[0]")
            # keep above 2 lines for applying more conditions.
            return self.UtilXml.getText(ele).strip()
        except:
            return None
            # raise Exception("Failed to get local string, please check element [" + str(element_name) + "] on [" + str(self.getCurrentPageName()) + "] page.")

    def _getLocatorValueByLocalString(self, element_name, locator_type,  locator_value):
        localString = self._getLocalStringFromFile(element_name, locator_type)
        if localString is None:
            return locator_value
        return self.__getReplacedLocatorByLocalString(locator_value, localString)
        # if element_name.endswith("_") and self.getLanguageRegion() != self.Language.en_US:
        #     localString = self._getLocalString(element_name)
        #     return self.__getReplacedLocatorByLocalString(locator_value, localString)
        # return locator_value

    def getLanguageRegion(self):
        return self.RunTimeConf.language + "_" + self.RunTimeConf.region

    def _isEmpty(self, obj):
        if obj == "" or obj is None:
            return True
        else:
            return False

    def _hasXpathText(self, str):
        return "".startswith("//") and ("(@" in str or "[@" in str)

    def loadTestDataFromExcel(self, name_sheet=None, path_file_excel=None):
        if self._DictTestData is None:
            self._HasSearchedTestData = True
            if path_file_excel is None:
                path_file_excel = self.path_file_xlsx_testData
            self._DictTestData = Exceller(path_file_excel, name_sheet).getDictTestData("placeholder")

    def getTestData(self, id):
        if self._DictTestData is not None:
            try:
                r = self._DictTestData[self.UtilString.toCodeName(id)]
                if r is None:
                    return "CanNotFind_" + id
                return r
            except:
                return "CanNotFind_" + id
        return "CanNotFind_" + id



