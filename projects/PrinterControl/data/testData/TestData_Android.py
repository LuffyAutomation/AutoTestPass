# coding: utf-8


class TestData_Android:
    def __init__(self, UI):
        self.Sheet_example = self._Sheet_example(UI)
    # sheet name: [sheet_example]
    class _sheet_example:
        # ID: [pageTitle] value:[in hand]
        pageTitle = 'pageTitle'
        # ID: [dp_msg_upload_success] value:[SuccessUpload App Successfully.]
        dp_msg_upload_success = 'dp_msg_upload_success'
        # ID: [dp_msg_upload_waiting] value:[WaitingThe server is parsing the files you uploaded. It won't take long, please wait a moment.]
        dp_msg_upload_waiting = 'dp_msg_upload_waiting'
