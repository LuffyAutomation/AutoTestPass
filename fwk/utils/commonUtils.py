# coding: utf-8
import os
import platform
# from configparser import ConfigParser
# try:
#     print platform.python_version()
#     import configparser
# except:
#     from six.moves import configparser
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Common:
    @staticmethod
    def getSection(conf):
        return conf.sections()

    @staticmethod
    def getConfigValue(conf, section, key):
     return conf.get(section, key)

    @staticmethod
    def getRoot(self):
        rootPath = os.getcwd() + os.sep
        return rootPath
    # @staticmethod
    # def configParser(path):
    #     conf = configparser.ConfigParser()
    #     conf.read(path, "utf-8")
    #     return conf


'''config = Common.configParser("D:/localGit/repositories/Python/ePint-Demo/resources/data/main.data")
value = config.get("ePrint","data.ePrint.Android")
print(value)
tree = Common.get_tree("D:/localGit/repositories/Python/ePint-Demo/resources/data/ePrint/uiMaps/Android/ePrint.xml")
root = Common.get_root_element(tree)
list = Common.get_element_by_xpath(root,".//AppName")
print(list.text)'''
'''
for index in range(len(list)):
    element = list[index]
    name = element.get("name")
    type = element.get("type")
    value = element.get("value")
    print(name)
    print(type)
    print(value)'''

'''tree = Common.get_tree("D:/localGit/repositories/Python/ePint-Demo/resources/data/ePrint/uiMaps/Android/ePrint.xml")
root = Common.get_root_element(tree)
list = Common.getEelements(root,".//page[@name='aa2']/element")
print(len(list))'''