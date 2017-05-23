# coding: utf-8


class TestData_Android:
    def __init__(self, UI):
        self.Sheet_example = self._Sheet_example(UI)
    # sheet name: [sheet_example]
    class _Sheet_example:
        def __init__(self, UI):
            self.UI = UI

        # ID: [pageTitle] value:[in hand]
        def pageTitle(self):
            return self.UI.getTestData('pageTitle')

        # ID: [dp_msg_upload_success] value:[SuccessUpload App Successfully.]
        def dp_msg_upload_success(self):
            return self.UI.getTestData('dp_msg_upload_success')

        # ID: [dp_msg_upload_waiting] value:[WaitingThe server is parsing the files you uploaded. It won't take long, please wait a moment.]
        def dp_msg_upload_waiting(self):
            return self.UI.getTestData('dp_msg_upload_waiting')
