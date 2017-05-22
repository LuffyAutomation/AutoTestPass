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
        NAME = "name"  # text
        ACCESSIBILITY_ID = "accessibility_id"  #1. content-desc 2. equal to name in some cases. But name has been depreated in appium 1.6
        TAG_NAME = "tag_name"
        CLASS_NAME = "class_name"
        CSS_SELECTOR = "css_selector"

    class AttributeType:
        NAME = "name"
        CLASS = "class"
        VALUE = "value"

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
        self._currentPage = None
        self._currentUiMap = None
        self._elementTimeOut = None
        self._getCurrentTestArgs(self.testType)
        self.__getConfigurationParameters()
        self.RunTimeConf = RunTimeConf(self.Init.ConfigParser)
        self._driver = None
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
            lambda start_time: self.__addLogForWaitEvent(method, "......%s %ss elapsed. Timeout is %ss. Interval is %s." % (log_prefix, start_time, time_out, poll_frequency)), error_message
        )
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
        self.setCurrentElementObject(None)
        return self

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

    def isEmpty(self, obj):
        if obj == "" or obj is None:
            return True
        else:
            return False

    DictTestData_current = None
    DictTestData_android = None
    DictTestData_ios = None
    DictTestData_web = None
    def __loadTestData(self, dictTestData, filePath, name_sheet=None, path_file_excel=None):
        if path_file_excel is None:
            path_file_excel = filePath
        if dictTestData is None:
            dictTestData = Exceller(path_file_excel, name_sheet).getDictTestData("placeholder")
        self.DictTestData_current = dictTestData
        return dictTestData

    def loadAndroidTestDataFromExcel(self, name_sheet=None, path_file_excel=None):
        self.DictTestData_android = self.__loadTestData(self.DictTestData_android, self.Init.path_file_xlsx_TestData_android, name_sheet,
                            path_file_excel)

    def loadIosTestDataFromExcel(self, name_sheet=None, path_file_excel=None):
        self.DictTestData_ios = self.__loadTestData(self.DictTestData_ios, self.Init.path_file_xlsx_TestData_ios, name_sheet,
                            path_file_excel)

    def loadWebTestDataFromExcel(self, name_sheet=None, path_file_excel=None):
        self.DictTestData_web = self.__loadTestData(self.DictTestData_web, self.Init.path_file_xlsx_TestData_web, name_sheet,
                            path_file_excel)

    def __getTestData(self, dictTestData, id):
        id = self.UtilString.toCodeName(id)
        if dictTestData is not None:
            try:
                r = dictTestData[id]
                if r is None:
                    return "CanNotFind_" + id
                return r
            except:
                return "CanNotFind_" + id

    def getTestDataAndroid(self, id):
        return self.__getTestData(self.DictTestData_android, id)

    def getTestDataIos(self, id):
        return self.__getTestData(self.DictTestData_ios, id)

    def getTestDataWeb(self, id):
        return self.__getTestData(self.DictTestData_web, id)
