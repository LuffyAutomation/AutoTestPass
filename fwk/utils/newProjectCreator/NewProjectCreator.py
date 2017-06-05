from fwk.base.InitFwk import InitFwk
import os

class NewProjectCreator:
    def __init__(self, name_project=None, testType=None):
        self.InitFwk = InitFwk(name_project.strip())
        self.InitFwk.testType = testType.strip().lower()

    def isProjectExisted(self):
        for name in self.InitFwk.list_all_projects:
            if self.InitFwk.name_project.lower() == name.lower():
                return True
        return False

    def fileContentReplace(self, path_file, old_text, new_text):
        if os.path.isfile(path_file):
            lines = open(path_file, self.InitFwk.UtilFile.FileMode.R).readlines()
            with open(path_file, self.InitFwk.UtilFile.FileMode.W) as f:
                _len = len(lines) - 1
                for i in range(_len):
                    lines[i] = lines[i].replace(old_text, new_text)
                    if self.InitFwk.testType.lower() == self.InitFwk.TestType.ANDROID.lower():
                        if ("_" + self.InitFwk.TestType.IOS.lower() in lines[i].lower() or "_" + self.InitFwk.TestType.WEB.lower() in lines[i].lower()) and "/" not in lines[i]:
                            lines[i] = "# " + lines[i]
                    elif self.InitFwk.testType.lower() == self.InitFwk.TestType.IOS.lower():
                        if ("_" + self.InitFwk.TestType.ANDROID.lower() in lines[i].lower() or "_" + self.InitFwk.TestType.WEB.lower() in lines[i].lower()) and "/" not in lines[i]:
                            lines[i] = "# " + lines[i]
                    elif self.InitFwk.testType.lower() == self.InitFwk.TestType.WEB.lower():
                        if ("_" + self.InitFwk.TestType.ANDROID.lower() in lines[i].lower() or "_" + self.InitFwk.TestType.IOS.lower() in lines[i].lower()) and "/" not in lines[i]:
                            lines[i] = "# " + lines[i]
                f.writelines(lines)

    def create(self):
        if self.isProjectExisted() is True:
            return
        self.InitFwk.UtilFolder.copyFolder(self.InitFwk.path_folder_PLACEHOLDER, os.path.join(self.InitFwk.path_folder_projects, self.InitFwk.name_project))
        self.InitFwk.UtilTime.sleep(1)
        # unittest file
        os.rename(os.path.join(self.InitFwk.path_folder_cases, self.InitFwk.Const.PLACEHOLDER + ".py"), os.path.join(self.InitFwk.path_folder_cases, self.InitFwk.name_project + ".py"))
        self.fileContentReplace(os.path.join(self.InitFwk.path_folder_cases, self.InitFwk.name_project + ".py"), self.InitFwk.Const.PLACEHOLDER, self.InitFwk.name_project)
        # start file
        self.InitFwk.UtilFile.copyFile(os.path.join(self.InitFwk.path_folder_templates, self.InitFwk.Const.PLACEHOLDER + ".py"), os.path.join(self.InitFwk.path_folder_AutoTestPass, "start_" + self.InitFwk.name_project + ".py"))
        self.InitFwk.UtilTime.sleep(1)
        self.InitFwk.UtilFile.fileContentReplace(os.path.join(self.InitFwk.path_folder_AutoTestPass, "start_" + self.InitFwk.name_project + ".py"), self.InitFwk.Const.PLACEHOLDER, self.InitFwk.name_project)
        # modify main conf
        self.InitFwk.ConfigParser.setMainConfigValue(self.InitFwk.ConfigParser.SECTION_DEFAULTPROJECT, self.InitFwk.ConfigParser.DEFAULT_PROJECT, self.InitFwk.name_project)
        self.InitFwk.ConfigParser.addProject(self.InitFwk.path_file_mainConf, self.InitFwk.name_project, self.InitFwk.testType)
        return self.InitFwk

