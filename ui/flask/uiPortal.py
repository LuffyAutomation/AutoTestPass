"""
RVFlask.py
Description: This module is background processing code about setting the configuration.
"""
from flask import Flask, render_template, request, redirect
import os
from fwk.base.InitFwk import InitFwk
from fwk.utils.newProjectCreator.NewProjectCreator import NewProjectCreator
import createPageObjects
import createTestDataStrings

_InitFwk = InitFwk()
errorMsg = ""
successMsg = ""
FLASK_ROOT_PATH = os.path.dirname(__file__)  # 'D:/Dev/DevicePass/script/AutoTestPass\\ui\\flask'
app = Flask(__name__)

# The default value for root path parameters of whole script
# app.config['PROJECT_ROOT'] = FLASK_ROOT_PATH

class UiPortal():
    result_rate_color_set = ["#4BC0C0", "#FF6384", "#FFCE56"]
    name_project = "name_project"
    action_selectProject = "action_selectProject"
    action_createPageObjects = "action_createPageObjects"
    action_createTestData = "action_createTestData"


    EDIT_NEWPROJECT = "edit_newProject"
    RADIOBUTTON_TESTTYPE = "radioButton_testType"

    def __init__(self):
        pass

    def reload_by_view(self, view_name):
        pass
_UiPortal = UiPortal()
# TODO----------------------------Drive------------------------------------------------------------------


@app.template_filter('space')
def space(value):
    return value.replace(' ', '&nbsp;')
# colorSet = [ "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", "#ABCABC"  ]
# "#FF6384","#4BC0C0","#FFCE56","#E7E9ED","#36A2EB"
# "Red","Green","Yellow","Grey","Blue"
# 8a6d3b

@app.route('/', methods=['GET', 'POST'])
def index():
    global _InitFwk, errorMsg, successMsg
    errorMsg = ""
    if request.method == 'GET':
        if _UiPortal.action_selectProject in request.args:
            _UiPortal.name_project = request.args[_UiPortal.action_selectProject]
            _InitFwk.ConfigParser.setMainConfigValue(_InitFwk.ConfigParser.SECTION_DEFAULTPROJECT, _InitFwk.ConfigParser.DEFAULT_PROJECT, _UiPortal.name_project)
            _InitFwk = InitFwk()
        elif _UiPortal.action_createPageObjects in request.args:
            createPageObjects.create()
            successMsg = "1. The Page Objects of <strong>%s</strong> are created successfully.</br>" % _InitFwk.name_project
        elif _UiPortal.action_createTestData in request.args:
            createTestDataStrings.create()
            successMsg = "1. The Test Data Objects of <strong>%s</strong> are created successfully.</br>" % _InitFwk.name_project
    elif request.method == 'POST':
        newProjectName = request.form[_UiPortal.EDIT_NEWPROJECT].strip()
        if newProjectName != "" and newProjectName is not None:
            testType = request.form[_UiPortal.RADIOBUTTON_TESTTYPE]
            _NewProjectCreator = NewProjectCreator(newProjectName, testType)
            _InitFwk = _NewProjectCreator.create()
            successMsg = "1. The Project <strong>%s</strong> is created successfully.</br>" % _InitFwk.name_project + \
                         "2. Please fill out <strong>%s</strong>.</br>" % os.path.join( _InitFwk.path_folder_data, "android or web or ios", "runTime.conf") + \
                         "3. Please fill out <strong>%s</strong> and then click <strong>Create Page Objects</strong> to create page objects.</br>" % os.path.join( _InitFwk.path_folder_data, "android or web or ios", "uiMaps", "uiMap.py") + \
                         "4. Please write Test Suite(cases) in <strong>%s</strong>.</br>" % os.path.join(_InitFwk.path_folder_cases, _InitFwk.name_project + ".py") + \
                         "5. Please add the names of Test cases that you want to test from the Test Suite to <strong>%s</strong>.</br>" % os.path.join(_InitFwk.path_folder_AutoTestPass, "(start_)" + _InitFwk.name_project + ".py")
        else:
            errorMsg = "<strong>New Project Name:</strong> cannot be empty!"
        _InitFwk = InitFwk()
    return render_template('index.html', _InitFwk=_InitFwk, errorMsg=errorMsg, successMsg=successMsg)

@app.route('/config', methods=['GET', 'POST'])
def config():
    """Display the index.html in the browser, post some new information to the decorator '/step-2'."""
    if request.method == 'POST':

        if _UiPortal.handleWhat == _UiPortal.event_edit:
            _UiPortal.handleWhat = ''
            return redirect('/setSettings')
        elif _UiPortal.handleWhat == _UiPortal.event_save:

            _UiPortal.handleWhat = ''
        elif _UiPortal.handleWhat == _UiPortal.event_editScanSettings:
            return redirect('/setLoopScan')
    return render_template('config.html', numRightList = _UiPortal.numberRightList, right_list = _UiPortal.listRightList, handleEvent = _UiPortal.handleWhat)

@app.route('/setLoopScan', methods=['GET', 'POST'])
def set_loopscan_settings():
    """Display the index.html in the browser, post some new information to the decorator '/step-2'."""
    if request.method == 'POST':
        return redirect('/config')
    return render_template('setLoopScan.html')
@app.route('/setSettings', methods=['GET', 'POST'])
def set_settings():
    """Display the index.html in the browser, post some new information to the decorator '/step-2'."""
    if request.method == 'POST':
        return redirect('/config')
    return render_template('setSettings.html')
@app.route('/step-2', methods=['GET', 'POST'])
def upload_file2():
    """Display the index-2.html in the browser, post some new information to the decorator '/showRS'."""
    if request.method == 'POST':
        app.config['resultDir'] = request.form['resPath']
        return redirect('/showRS')
    else:
        if os.path.exists(app.config['PROJECT_ROOT']):
            return render_template('index-2.html', b_flag='active')
        else:
            return render_template('index-2.html', resultDirs=["Can't find result dir"], b_flag='active')

@app.route('/exTestConfig', methods=['GET', 'POST'])
def ex_test_config1():
    """Display the cbTestConfig1.html in the browser, post some new information to the decorator '/exTestConfig2'."""
    if request.method == 'POST':
        #exData.dut1['PrinterOneSeries'] = request.form['PrinterOneSeries']
        return redirect('/exTestConfig2')
    return render_template('cbTestConfig1.html', air_ex_Test=True, et_flag='active', sm_flag='active')
