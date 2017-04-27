from src.utils.poCreator.POCreator import POCreator

if __name__ == '__main__':
    # POCreator = POCreator(
    #     r"D:\Dev\DevicePass\script\AutoTestPass\src\project\PrinterControl\data\android\uiMaps\printerControl.xml",
    #     r"D:\Dev\DevicePass\script\AutoTestPass\src\project\PrinterControl\po")
    # POCreator.create()
    project = "PrinterControl"
    POCreator = POCreator(
        r"D:\Dev\DevicePass\script\AutoTestPass\project\%s\data\android\uiMaps\%s.xml" % (project, project),
        r"D:\Dev\DevicePass\script\AutoTestPass\project\%s\po" % project)
    POCreator.create()