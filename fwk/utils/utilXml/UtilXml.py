# try:
#     import xml.etree.cElementTree as etree
# except ImportError:
#     import xml.etree.ElementTree as etree
from lxml import etree


class UtilXml:
    @staticmethod
    def get_tree(xml_path):
        tree = etree.parse(xml_path)
        return tree
    @staticmethod
    def get_root_element(tree):
        return tree.getroot()
    @staticmethod
    def get_tag_name(element):
        return element.tag
    @staticmethod
    def get_text(element):
        return element.text
    @staticmethod
    def get_attribute(element):
        return element.attrib
    @staticmethod
    def get_children(element):
        return element.getchildren()
    @staticmethod
    def get_elements(element, xpath):
        return element.findall(xpath)
    @staticmethod
    def get_element(element, xpath):
        return element.find(xpath)
    @staticmethod
    def get_element_by_xpath(root, xpath):
        """Find all matching subelements by tag name or path.

        *path* is a string having either an element tag or an XPath,
        *namespaces* is an optional mapping from namespace prefix to full name.

        Returns list containing all matching elements in document order.

        """
        list = root.findall(xpath)

        if len(list) > 1:
            print("The duplicate node exists.")
        else:
            return list[0]

    @staticmethod
    def get_element_text(element):
        return element.text

    @staticmethod
    def get_list_by_xpath(tree, xpath):
        t_list = tree.xpath(xpath)
        return t_list
