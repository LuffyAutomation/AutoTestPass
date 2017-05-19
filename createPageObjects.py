import os
from fwk.base.InitFwk import InitFwk
from fwk.utils.poCreator.POCreator import POCreator

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def create():
    # project is defined in env>main.conf>[DefaultProject].
    _InitFwk = InitFwk()
    _POCreator = POCreator(_InitFwk.path_file_xml_uiMap_android, _InitFwk.path_folder_po)
    _POCreator.create()
    _POCreator = POCreator(_InitFwk.path_file_xml_uiMap_web, _InitFwk.path_folder_po)
    _POCreator.create()
    _POCreator = POCreator(_InitFwk.path_file_xml_uiMap_ios, _InitFwk.path_folder_po)
    _POCreator.create()

if __name__ == '__main__':
    create()

