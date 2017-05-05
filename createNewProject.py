import os
from fwk.base.InitFwk import InitFwk
from fwk.utils.poCreator.POCreator import POCreator

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

if __name__ == '__main__':
    # project is defined in env>main.conf>[DefaultProject].

    initFwk = InitFwk()
    _POCreator = POCreator(initFwk._path_folder_uiMaps_android, initFwk._path_folder_po)
    _POCreator.create()
    _POCreator = POCreator(initFwk._path_folder_uiMaps_web, initFwk._path_folder_po)
    _POCreator.create()
    _POCreator = POCreator(initFwk._path_folder_uiMaps_ios, initFwk._path_folder_po)
    _POCreator.create()
