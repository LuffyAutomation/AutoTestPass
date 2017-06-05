# from InitFwk import InitFwk
import os

from selenium.webdriver.common.by import By
from fwk.utils.exceller.Exceller import Exceller
from fwk.other.RunTimeConf import RunTimeConf
from fwk.utils.utilTime.UtilWaitEvent import UtilWaitEvent


class UiBaseFwk(object):
    class StringConverter:
        VALUE_PLACEHOLDER = 'VALUE_PLACEHOLDER'
        MARK_DYNAMIC_VALUE = ' : '

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

    class LocatorType:
        ID = "id"
        XPATH = "xpath"
        LINK_TEXT = "link_text"
        PARTIAL_LINK_TEXT = "partial_link_text"
        #NAME = "name"  # text, but name has been depreated in appium 1.6
        ACCESSIBILITY_ID = "accessibility_id"  #1. content-desc 2. equal to name in some cases. But name has been depreated in appium 1.6
        TAG_NAME = "tag_name"
        CLASS_NAME = "class_name"
        CSS_SELECTOR = "css_selector"

    class AttributeType:
        NAME = "name"
        CLASS = "class"
        VALUE = "value"
        CHECKED = 'checked'

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
        self._root = None
        self._rootLocalXml = None

        self._currentElementName = None
        self._currentElementObject = None

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

        # if 2 == 1:
        #     self.Init = InitFwk
        #     self._driver = webdriver.Remote("")

    def __getConfObject(self, configFileName):
        return self.Init.ConfigParser.getConf(configFileName)

    def _getCurrentTestArgs(self, testType):
        try:
            self._path_file_runTimeConf = os.path.join(self.Init.path_folder_data, testType, 'runTime.conf')
        except:
            if testType is None:
                self.logger.error("faild to find [%s] in [%s]." % (self.Init._name_project, self.Init._path_file_mainConf))

        self.__RunTimeConfig = self.__getConfObject(self._path_file_runTimeConf)
        self.Init.ConfigParser.setRunTimeConfig(self.__RunTimeConfig)
        self._path_folder_uiMaps = os.path.join(self.Init.path_folder_data, testType, 'uiMaps')
        self._path_file_uiMap = os.path.join(self._path_folder_uiMaps, self.Init.ConfigParser.getRunTimeConfigArgsValue(self.Init.ConfigParser.TEST_UIMAP_FILENAME))

    def __getConfigurationParameters(self):
        self._xmlTree = self.UtilXml.getTree(self._path_file_uiMap)
        self._root = self.UtilXml.getRootElement(self._xmlTree)
        self._elementTimeOut = self.Init.ConfigParser.getRunTimeConfigArgsValue(self.Init.ConfigParser.TEST_TIMEOUT_ELEMENT)

    def __addLogForWaitEvent(self, method, log):
        if ". 0s elapsed" not in log:  # ignore this
            self.logger.info(log)
        return method()

    def waitUntil(self, method, error_message="Wait failed.", time_out=None, poll_frequency=2, log_prefix=None):
        if log_prefix is None:
            log_prefix = "Finding element [" + str(self.getCurrentElementName()) + "] of page [" + str(self.getCurrentPage()) + "]."
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

    def _getUiMapRoot(self):
        return self._root

    def updateCurrentElementStatus(self, element_name, uiMap, currentPage):
        if self._currentElementName != element_name:
            self._currentElementObject = None
        if self._currentElementCollectionName != element_name:
            self._currentElementCollectionName = None
        self._currentUiMap = uiMap
        self._currentPage = currentPage
        self._currentElementName = element_name
        return self

    # if define VALUE_PLACEHOLDER in uimap:
    # <element name="text_printerIp" page="page_home"><xpath>//android.widget.TextView[contains(@text,'VALUE_PLACEHOLDER')]</xpath></element>
    # you can find the element by  xxx.replacePlaceholder("10").click
    def replacePlaceholder(self, dynamic_value, element_name=None):
        element_name = self._getCurrentElementNameWhenNone(element_name)
        self._currentElementName = element_name + self.StringConverter.MARK_DYNAMIC_VALUE + dynamic_value
        return self

    #some elements' status may change after they appear. So need to clear the found ele and re-find.
    def refreshMe(self):
        self.setCurrentElementObject(None)
        self.setCurrentElementCollectionObject(None)
        return self

    def setCurrentElementName(self, element_name):
        self._currentElementName = element_name

    def getCurrentElementName(self):
        return self._currentElementName

    def setCurrentElementObject(self, element=None):
        self._currentElementObject = element

    def getCurrentElementObject(self):
        return self._currentElementObject

    def setCurrentElementCollectionName(self, elementCollection_name):
        self._currentElementCollectionName = elementCollection_name

    def getCurrentElementCollectionName(self):
        return self._currentElementCollectionName

    def setCurrentElementCollectionObject(self, element=None):
        self._currentElementCollectionObject = element

    def getCurrentElementCollectionObject(self):
        return self._currentElementCollectionObject

    def _setCurrentPage(self, page):
        self._currentPage = page

    def getCurrentPage(self):
        return self._currentPage

    def _getElementType(self, element_locators_list):
        return element_locators_list[0]

    def _getElementValue(self, element_locators_list):
        return element_locators_list[1]

    def _getElementIndex(self, element_locators_list):
        t = element_locators_list[2]
        try:
            return int(t) - 1
        except:
            return 0

    # for log
    def _getCurrentElementNameWhenNone(self, element_name=None):
        if element_name == None:
            element_name = self.getCurrentElementName()
        return element_name

    def _getElementObjectFromCurrentOrSearch(self, idx_or_match=None, element_name=None):
        if self.getCurrentElementObject() is not None:
            return self.getCurrentElementObject()
        self.setCurrentElementObject(self.getMatchedElement(idx_or_match, self.getCurrentElementName()))
        return self.getCurrentElementObject()

    def _getCurrentElementCollectionName(self, element_name=None):
        if element_name == None:
            element_name = self.getCurrentElementCollectionName()
        return element_name

    def _getElementCollectionObjectFromCurrentOrSearch(self, idx_or_match=None, element_name=None):
        if self.getCurrentElementCollectionObject() is not None:
            return self.getCurrentElementCollectionObject()
        self.setCurrentElementCollectionObject(self.getMatchedElements(idx_or_match, self.getCurrentElementName()))
        return self.getCurrentElementCollectionObject()

    def _getElementLocatorsList(self, element_name):
        dynamic_string = None
        ori_element_name = element_name
        if self.StringConverter.MARK_DYNAMIC_VALUE in element_name:
            dynamic_string = element_name.split(self.StringConverter.MARK_DYNAMIC_VALUE)[1]
            element_name = element_name.split(self.StringConverter.MARK_DYNAMIC_VALUE)[0]
        locators = self._currentUiMap.get(element_name)['locators']
        list = []
        for locator in locators:
            locator_type = self.UtilXml.getTagName(locator)
            locator_type = self.__get_sys_locator_type(locator_type)
            locator_value = self.UtilXml.getText(locator).strip()
            global locator_index
            try:
                locator_index = self.UtilXml.getAttribute(locator)['index']
            except:
                locator_index = "1"
            if dynamic_string is not None and self.StringConverter.VALUE_PLACEHOLDER in locator_value:
                locator_value = locator_value.replace(self.StringConverter.VALUE_PLACEHOLDER, dynamic_string)
            #self.logger.info("............Finding element [" + element_name + "] of page [" + str(self.getCurrentPage()) + "]. locator_type is [" + locator_type + "] locator_value is [" + locator_value + "].")
            list.append([locator_type, locator_value, locator_index])
        if locators == None:
            raise Exception("Can not find element [" + ori_element_name + "] on [" + str(self._currentPage) + "] page.")
        return list

    def __get_sys_locator_type(self, locator_type):
        if locator_type == self.LocatorType.ID:
            locator_type = By.ID
        # elif locator_type == self.LocatorType.NAME:
        #     locator_type = By.NAME # it is deprecated in 1.5
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

    def _getLocalString(self, element_name):
        try:
            ele = self.UtilXml.getElement(self._rootLocalXml, ".//page[@name='"+self.getCurrentPage()+"']/element[@name='"+element_name+"']")
            return self.UtilXml.getText(ele).strip()
        except:
            raise Exception("Failed to get local string, please check element [" + str(element_name) + "] on [" +str(self.getCurrentPage()) + "] page.")

    def _getLocatorValueByLocalString(self, element_name, locator_value):
        if element_name.endswith("_") and self.getLanguageRegion() != self.Language.en_US:
            localString = self.__getLocalString(element_name)
            return self.__getReplacedLocatorByLocalString(locator_value, localString)
        return locator_value

    def getLanguageRegion(self):
        return self.RunTimeConf.language + "_" + self.RunTimeConf.region

    def _isEmpty(self, obj):
        if obj == "" or obj is None:
            return True
        else:
            return False

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



