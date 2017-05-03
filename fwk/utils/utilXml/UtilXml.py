try:
    import xml.etree.cElementTree as et
except ImportError:
    import xml.etree.ElementTree as et


class UtilXml:

    @staticmethod
    def getTree(xml_path):
        tree = et.parse(xml_path)
        return tree
    @staticmethod
    def getRootElement(tree):
        return tree.getroot()
    @staticmethod
    def getTagName(element):
        return element.tag
    @staticmethod
    def getText(element):
        return element.text
    @staticmethod
    def getAttribute(element):
        return element.attrib
    @staticmethod
    def getChildren(element):
        return element.getchildren()
    @staticmethod
    def getElements(element, xpath):
        return element.findall(xpath)
    @staticmethod
    def getElement(element, xpath):
        return element.find(xpath)
    @staticmethod
    def getElementByXpath(root, xpath):
        """Find all matching subelements by tag name or path.

        *path* is a string having either an element tag or an XPath,
        *namespaces* is an optional mapping from namespace prefix to full name.

        Returns list containing all matching elements in document order.

        """

        list = root.findall(xpath)

        if len(list) > 1:
            print("The duplicate note exists.")
        else:
            return list[0]

    @staticmethod
    def getEelmentText(element):
        return element.text