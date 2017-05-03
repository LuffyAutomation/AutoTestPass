import os

from fwk.utils.poCreator.POCreator import POCreator

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

if __name__ == '__main__':
    # Only next row needs to be modified according to your existed projects name.
    project = "PrinterControl"
    #project = "WebExample"




    path_folder_po = os.path.join(PATH(""), "projects", project, "po")
    path_folder_data = os.path.join(PATH(""), "projects", project, "data")
    path_folder_p = os.path.join("uiMaps", "uiMap.xml")
    path_folder_uiMaps = os.path.join(path_folder_data, "android", path_folder_p)
    _POCreator = POCreator(path_folder_uiMaps, path_folder_po)
    _POCreator.create()
    path_folder_uiMaps = os.path.join(path_folder_data, "web", path_folder_p)
    _POCreator = POCreator(path_folder_uiMaps, path_folder_po)
    _POCreator.create()
    path_folder_uiMaps = os.path.join(path_folder_data, "ios", path_folder_p)
    _POCreator = POCreator(path_folder_uiMaps, path_folder_po)
    _POCreator.create()
