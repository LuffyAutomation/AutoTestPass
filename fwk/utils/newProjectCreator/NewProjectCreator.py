from fwk.base.InitFwk import InitFwk
import os

class NewProjectCreator:
    def __init__(self, name_project=None, testType=None):
        self.InitFwk = InitFwk(name_project)
        self.InitFwk.testType = testType

    def isProjectExisted(self):
        for name in self.InitFwk.list_all_projects:
            if self.InitFwk.name_project.lower() == name.lower():
                return True
        return False

    def create(self):
        if self.isProjectExisted() is True:
            return
        self.InitFwk.UtilFolder.copyFolder(self.InitFwk.path_folder_PLACEHOLDER, os.path.join(self.InitFwk.path_folder_projects, self.InitFwk.name_project))
        self.InitFwk.UtilTime.sleep(1)
        # unittest file
        os.rename(os.path.join(self.InitFwk.path_folder_cases, self.InitFwk.Const.PLACEHOLDER + ".py"), os.path.join(self.InitFwk.path_folder_cases, self.InitFwk.name_project + ".py"))
        self.InitFwk.UtilFile.fileContentReplace(os.path.join(self.InitFwk.path_folder_cases, self.InitFwk.name_project + ".py"), self.InitFwk.Const.PLACEHOLDER, self.InitFwk.name_project)
        # start file
        self.InitFwk.UtilFile.copyFile(os.path.join(self.InitFwk.path_folder_templates, self.InitFwk.Const.PLACEHOLDER + ".py"), os.path.join(self.InitFwk.path_folder_AutoTestPass, "start_" + self.InitFwk.name_project + ".py"))
        self.InitFwk.UtilTime.sleep(1)
        self.InitFwk.UtilFile.fileContentReplace(os.path.join(self.InitFwk.path_folder_AutoTestPass, "start_" + self.InitFwk.name_project + ".py"), self.InitFwk.Const.PLACEHOLDER, self.InitFwk.name_project)
        # modify main conf
        self.InitFwk.ConfigParser.setMainConfigValue(self.InitFwk.ConfigParser.SECTION_DEFAULTPROJECT, self.InitFwk.ConfigParser.DEFAULT_PROJECT, self.InitFwk.name_project)
        self.InitFwk.ConfigParser.addProject(self.InitFwk.path_file_mainConf, self.InitFwk.name_project, self.InitFwk.testType)

