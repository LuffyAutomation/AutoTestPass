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
        # list = (en_US)

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

        def get_page_name(self):
            return self.page_name

        def get_page_uiMap(self):
            return self.page_uiMap

        def get_name(self):
            return self.name

        def get_object(self):
            return self.object

        def get_index(self):
            return self.index

        def get_list_locators(self):
            return self.list_locators

        def set_page_name(self, page_name):
            self.page_name = page_name

        def set_page_uiMap(self, page_uiMap):
            self.page_uiMap = page_uiMap

        def set_name(self, name):
            self.name = name

        def set_object(self, object):
            self.object = object

        def set_index(self, index):
            self.index = index

        def get_list_locators(self, list_locators):
            self.list_locators = list_locators

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
        self.ActionElement = self.ElementStruct()
        self.LastElement = self.ElementStruct()
        self.CurrentElementCollection = self.ElementStruct()
        self.RefElement = self.ElementStruct()

        self._elementTimeOut = None
        self._get_current_test_args(self.testType)
        self.__get_config_parameters()
        self.RunTimeConf = RunTimeConf(self.Init.ConfigParser)
        self._driver = None

        self.path_file_xlsx_testData = ""
        self._DictTestData = None
        self._HasSearchedTestData = False

        self.hasGotDriver = False

        self._last_log_info = ""
        self._last_log_warning = ""
        self._last_log_error = ""

    def __get_config_object(self, name_config_file):
        return self.Init.ConfigParser.getConf(name_config_file)

    def _get_current_test_args(self, testType):
        try:
            # local pc /opt/devicepass/android/automation-workspace/1adaa521831046b985b39f5ea27b30b3/python-work-HC43YWW01974/projects/PrinterControl/data/Android/runTime.conf
            # both Android/ android are right. But in DP Android will fail.
            testType = testType.lower()
            self._path_file_runTimeConf = os.path.join(self.Init.path_folder_data, testType, 'runTime.conf')
        except:
            if testType is None:
                self.logger.error("Failed to find [%s] from [%s]." % (self.Init._name_project, self.Init._path_file_mainConf))
        self.__RunTimeConfig = self.__get_config_object(self._path_file_runTimeConf)
        self.Init.ConfigParser.setRunTimeConfig(self.__RunTimeConfig)
        self._path_folder_uiMaps = os.path.join(self.Init.path_folder_data, testType, 'uiMaps')
        self._path_file_uiMap = os.path.join(self._path_folder_uiMaps, self.Init.ConfigParser.getRunTimeConfigArgsValue(self.Init.ConfigParser.TEST_UIMAP_FILENAME))
        self.language = self.Init.ConfigParser.getRunTimeConfigArgsValue(self.Init.ConfigParser.TEST_LANGUAGE)
        if self.language is None:
            self.logger.error("[%s] was not listed in [%s]." % (self.Init.ConfigParser.TEST_LANGUAGE, self._path_file_runTimeConf))
            raise "[%s] was not listed in [%s]." % (self.Init.ConfigParser.TEST_LANGUAGE, self._path_file_runTimeConf)
        self._path_file_uiMap_localized = os.path.join(self._path_folder_uiMaps, self.language)
        if not self._path_file_uiMap_localized.lower().endswith(".xml"):
            self._path_file_uiMap_localized += ".xml"

    def get_language(self):
        return self.language

    def __get_config_parameters(self):
        self._xmlTree = self.UtilXml.get_tree(self._path_file_uiMap)
        self._xmlRoot = self.UtilXml.get_root_element(self._xmlTree)
        self._elementTimeOut = self.Init.ConfigParser.getRunTimeConfigArgsValue(self.Init.ConfigParser.TEST_TIMEOUT_ELEMENT)

        self._xmlTree_localized = None
        self._xmlRoot_localized = None
        try:
            self._xmlTree_localized = self.UtilXml.get_tree(self._path_file_uiMap_localized)
            self._xmlRoot_localized = self.UtilXml.get_root_element(self._xmlTree_localized)
        except:
            self.logger.warning("Please make sure if [%s] is existing. Or Please check if the [test.language=] is set correctly in runTime.conf." % (self._path_file_uiMap_localized))

    def logger_warning_save(self, msg):
        self._last_log_warning = msg
        self.logger.warning(msg)

    def logger_error_save(self, msg):
        self._last_log_error = msg
        self.logger.error(msg)

    def logger_info_save(self, msg):
        self._last_log_info = msg
        self.logger.info(msg)

    def get_last_log_info(self):
        return self._last_log_info

    def get_last_log_error(self):
        return self._last_log_error

    def get_last_log_warning(self):
        return self._last_log_warning

    def __add_log_for_wait_event(self, method, log):
        if ". 0s elapsed" not in log:  # ignore this
            self.logger.info(log)
        return method()

    def wait_until(self, method, error_message="Wait failed.", time_out=None, poll_frequency=2, log_prefix=None):
        if log_prefix is None:
            log_prefix = "Finding element [" + str(self.get_current_element_name()) + "] of page [" + str(self.get_current_page_name()) + "]."
        if time_out is None:
            try:
                time_out = float(self._elementTimeOut)
            except Exception:
                time_out = 60
        try:
            self.UtilWaitEvent(time_out, poll_frequency).until(
                lambda elapsed_time: self.__add_log_for_wait_event(method, "......%s %ss elapsed. Timeout is %ss. Interval is %ss." % (log_prefix, elapsed_time, time_out, poll_frequency))
            )
        except Exception:
            raise Exception("%s in %ds." % (error_message, error_message))

    def wait(self, time):
        try:
            # self.logger.info("Wait " + str(time) + "s.")
            self.UtilTime.sleep(time)
        except Exception:
            pass
        return self

    def get_uimap(self, page):
        xpath = ".//page[@name='"+page+"']/element"
        return self.get_uimap_by_xpath(xpath)

    def get_uimap_of_subpage(self, page, subPage):
        xpath = ".//page[@name='"+page+"']/page[@name='"+subPage+"']/element"
        return self.get_uimap_by_xpath(xpath)

    def get_uimap_by_xpath(self, xpath):
        list = self.UtilXml.get_elements(self._xmlRoot, xpath)
        currentElements = {}
        for index in range(len(list)):
            attributes = self.UtilXml.get_attribute(list[index])
            children = self.UtilXml.get_children(list[index])
            name = attributes.get("name")
            attributes["locators"] = children
            currentElements[name] = attributes
        if len(list) == len(currentElements):
            return currentElements
        else:
            raise Exception("There are duplicated pages existing. [" + xpath + "].")

    def _get_uimap_root(self):
        return self._xmlRoot

    def get_page_names_from_uimap(self, xpath='.//page/@name'):
        return self.UtilXml.get_list_by_xpath(self._get_uimap_root(), xpath)

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
    # you can find the element by  xxx.replace_placeholder("10").click
    def replace_placeholder(self, dynamic_value, element_name=None):
        element_name = self._get_current_element_name_when_none(element_name)
        self.CurrentElement.name = element_name + self.StringConverter.MARK_DYNAMIC_VALUE + dynamic_value
        return self

    #some elements' status may change after they appear. So need to clear the found ele and re-find.
    def refresh_element(self):
        self.set_current_element_object(None)
        self.set_current_element_collection_object(None)
        return self

    def set_current_element_name(self, element_name):
        self.CurrentElement.name = element_name

    def get_current_element_name(self):
        return self.CurrentElement.name

    def set_current_element_object(self, element=None):
        self.CurrentElement.object = element

    def set_current_element_index(self, index=None):
        self.CurrentElement.index = index

    def get_current_element_object(self):
        return self.CurrentElement.object

    def get_last_element_name(self):  # when using this kind of method  .swithToElement
        return self.LastElement.name

    def get_last_element_object(self):
        return self.LastElement.object

    def set_last_element_object(self, element=None):
        self.LastElement.object = element

    def set_current_element_collection_name(self, elementCollection_name):
        self.CurrentElementCollection.name = elementCollection_name

    def set_current_element_collection_index(self, elementCollection_index):
        self.CurrentElementCollection.index = elementCollection_index

    def get_current_element_collection_name(self):
        return self.CurrentElementCollection.name

    def set_current_element_collection_object(self, element=None):
        self.CurrentElementCollection.object = element

    def get_current_element_collection_object(self):
        return self.CurrentElementCollection.object

    def _set_current_page_name(self, page_name):
        self.CurrentElement.page_name = page_name

    def get_current_page_name(self):
        return self.CurrentElement.page_name

    def _get_element_type(self, element_locators_list):
        return element_locators_list[self.Locator.TYPE]

    def _get_element_value(self, element_locators_list):
        return element_locators_list[self.Locator.VALUE]

    def _get_element_index(self, element_locators_list):
        t = element_locators_list[self.Locator.INDEX]
        try:
            return int(t)
        except:
            return 1

    def _set_action_element(self, idx_or_match=None, element_name=None):
        if element_name is None:
            element_name = self.CurrentElement.get_name()
            if element_name is None:
                return
                # self.Pages.Page_home.open_main_page()  <   No element
        if type(element_name) is not str:  # ElementStruct
            element_name = element_name.get_name()
            element_object = element_name.get_object()
        elif self.CurrentElement.get_name() == element_name and self.CurrentElement.get_object() is not None:
            element_object = self.CurrentElement.get_object()
        else:
            element_object = self.getMatchedElement(idx_or_match, element_name)
            self.CurrentElement.set_object(element_object)
        self.ActionElement.set_name(element_name)
        self.ActionElement.set_object(element_object)
        self.ActionElement.set_page_name(self.CurrentElement.get_page_name())

    # for log
    def _get_current_element_name_when_none(self, element_name=None):
        if element_name is None:
            element_name = self.get_current_element_name()
        if type(element_name) is not str:  # ElementStruct
            return element_name.name
        return element_name

    def _get_current_element_object_or_search(self, idx_or_match=None, element_name=None):
        if element_name is not None:
            if type(element_name) is not str:  #  ElementStruct
                return element_name.object
            if self.CurrentElement.name == element_name and self.get_current_element_object() is not None:
                return self.get_current_element_object()
        elif self.get_current_element_object() is not None:
            return self.get_current_element_object()
        self.set_current_element_object(self.getMatchedElement(idx_or_match, self.get_current_element_name()))
        return self.get_current_element_object()

    def _get_last_element_object_or_search(self, idx_or_match=None, element_name=None):
        if type(element_name) is not str:  # ElementStruct
            return element_name
        if self.get_last_element_object() is not None and self.LastElement.name == element_name:
            return self.get_last_element_object()
        self.set_last_element_object(self.getMatchedElement(idx_or_match, element_name))
        return self.get_last_element_object()

    def _get_current_element_collection_name(self, element_name=None):
        if element_name == None:
            element_name = self.get_current_element_collection_name()
        return element_name

    def _get_element_collection_object_from_current_or_search(self, idx_or_match=None, element_name=None):
        if self.get_current_element_collection_object() is not None:
            return self.get_current_element_collection_object()
        self.set_current_element_collection_object(self.getMatchedElements(idx_or_match, self.get_current_element_name()))
        return self.get_current_element_collection_object()

    def _get_element_locators_dict_list(self, element_name, WhichElement=None):
        dynamic_string = None
        ori_element_name = element_name
        if WhichElement is None:
            WhichElement = self.CurrentElement
        if self.StringConverter.MARK_DYNAMIC_VALUE in element_name:
            dynamic_string = element_name.split(self.StringConverter.MARK_DYNAMIC_VALUE)[1]
            element_name = element_name.split(self.StringConverter.MARK_DYNAMIC_VALUE)[0]
        uiMapByName = WhichElement.page_uiMap.get(element_name)
        if uiMapByName is None:
            raise Exception("Can not find the element [{}] listed in ui map [{}].".format(element_name, self.CurrentElement.get_page_name()))
        locators = uiMapByName['locators']
        locator_ref = None
        try:
            locator_ref = uiMapByName[self.Locator.REF]
        except:
            pass
        list = []
        for locator in locators:
            locator_type = self.UtilXml.get_tag_name(locator)
            locator_type = self._get_native_locator_type(locator_type)
            locator_value = self.UtilXml.get_text(locator).strip()
            locator_value = self._get_locator_value_by_local_string(element_name, locator_type, locator_value)
            global locator_index
            try:
                locator_index = self.UtilXml.get_attribute(locator)['index']
            except:
                locator_index = "1"
            if dynamic_string is not None and self.StringConverter.VALUE_PLACEHOLDER in locator_value:
                locator_value = locator_value.replace(self.StringConverter.VALUE_PLACEHOLDER, dynamic_string)
            #self.logger.info("............Finding element [" + name + "] of page [" + str(self.getCurrentPage()) + "]. locator_type is [" + locator_type + "] locator_value is [" + locator_value + "].")
            list.append({self.Locator.TYPE: locator_type, self.Locator.VALUE: locator_value, self.Locator.INDEX: locator_index, self.Locator.REF: locator_ref})
        if locators == None:
            raise Exception("Can not find the element [" + ori_element_name + "] on the screen [" + str(self.CurrentElement.page_name) + "].")
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

    def __get_replaced_locator_by_local_string(self, locator_value, local_string):
        if self._has_xpath_text(local_string):
            return local_string

        matcher_array = [locator_value]
        if "(@" in locator_value:
            matcher_array = re.findall("\'([^\"]*)\'\)\]", locator_value)
            if matcher_array.__len__() == 0:
                matcher_array = re.findall("\"([^\"]*)\"\)\]", locator_value)
                if matcher_array.__len__() == 0:
                    raise Exception("The xpath [" + locator_value + "] for the element [" + str(self.get_current_element_name()) + "] is unavailable.")
        elif "[@" in locator_value:
            matcher_array = re.findall("\'([^\"]*)\'\]", locator_value)
            if matcher_array.__len__() == 0:
                matcher_array = re.findall("\"([^\"]*)\"\]", locator_value)
                if matcher_array.__len__() == 0:
                    raise Exception("The xpath [" + locator_value + "] for the element [" + str(self.get_current_element_name()) + "] is unavailable.")
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

    def _get_local_string_from_file(self, element_name, locator_type):
        if self._xmlRoot_localized is None:
            return None
        try:
            t_page_name = self.get_current_page_name()
            if "\\" in t_page_name:
                list_page_name = t_page_name.split("\\")
                t_page_name = list_page_name[0] + "']/page[@name='" + list_page_name[1]
            ele = self.UtilXml.get_element(self._xmlRoot_localized, ".//page[@name='" + t_page_name + "']/element[@name='" + element_name + "']/%s" % locator_type)
            # if ele is None:  # Maybe the locator_type from uiMap is unmatched with the corresponding one from localized uiMap.
            #     ele = self.UtilXml.get_element(self._xmlRoot_localized, ".//page[@name='" + self.get_current_page_name() + "']/element[@name='" + element_name + "']/*[0]")
            # keep above 2 lines for applying more conditions.
            return self.UtilXml.get_text(ele).strip()
        except:
            return None
            # raise Exception("Failed to get local string, please check element [" + str(element_name) + "] on [" + str(self.get_current_page_name()) + "] page.")

    def _get_locator_value_by_local_string(self, element_name, locator_type, locator_value):
        localString = self._get_local_string_from_file(element_name, locator_type)
        if localString is None:
            return locator_value
        return self.__get_replaced_locator_by_local_string(locator_value, localString)
        # if element_name.endswith("_") and self.get_language_region() != self.Language.en_US:
        #     localString = self._getLocalString(element_name)
        #     return self.__get_replaced_locator_by_local_string(locator_value, localString)
        # return locator_value

    def get_language_region(self):
        return self.RunTimeConf.language + "_" + self.RunTimeConf.region

    def _is_empty(self, obj):
        if obj == "" or obj is None:
            return True
        else:
            return False

    def _has_xpath_text(self, str):
        return "".startswith("//") and ("(@" in str or "[@" in str)

    def load_test_data_from_excel(self, name_sheet=None, path_file_excel=None):
        if self._DictTestData is None:
            self._HasSearchedTestData = True
            if path_file_excel is None:
                path_file_excel = self.path_file_xlsx_testData
            self._DictTestData = Exceller(path_file_excel, name_sheet).getDictTestData("placeholder")

    def get_test_data(self, id):
        if self._DictTestData is not None:
            try:
                r = self._DictTestData[self.UtilString.toCodeName(id)]
                if r is None:
                    return "CanNotFind_" + id
                return r
            except:
                return "CanNotFind_" + id
        return "CanNotFind_" + id

    def get_items_count(self):
        try:
            if self.get_current_element_name() != self.get_current_element_collection_name():
                self._get_current_element_object_or_search(None, None)
                self._get_current_element_name_when_none(None)
                return len(self.get_current_element_collection_object())
        except:
            return 0
            # raise Exception("Can not get children count of element [" + self.get_current_element_collection_name() + "] on [" + str(self.CurrentElement.page_name) + "] page.")

    def get_items(self):
        try:
            if self.get_current_element_name() != self.get_current_element_collection_name():
                self._get_element_collection_object_from_current_or_search(None, None)
                self._get_current_element_collection_name(None)
            # self.set_current_element_name(self.get_current_element_collection_name())
            # self.set_current_element_object(self.get_current_element_collection_object())
            return self
        except:
            raise Exception("Can not find all of element [" + self.get_current_element_collection_name() + "] on the screen [" + str(self.CurrentElement.page_name) + "].")

    def get_item(self, child_element_index):
        try:
            if self.get_current_element_name() != self.get_current_element_collection_name():
                self._get_current_element_object_or_search(None, None)
                self._get_current_element_name_when_none(None)
            self.set_current_element_name(self.get_current_element_collection_name() + "_index_" + str(child_element_index))
            self.set_current_element_object(self.get_current_element_collection_object()[child_element_index - 1])
            return self
        except:
            raise Exception("Can not find the element [" + self.get_current_element_collection_name() + "] with index [" + str(child_element_index) + "] on the screen [" + str(self.CurrentElement.page_name) + "].")