from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import loadingProgress_UI

class LoadingProgressDialog(QDialog):

    progress_updated = Signal(int)    #커스텀 시그널 정의    

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = loadingProgress_UI.Ui_Dialog_loadingProg()
        # 커스텀 시그널을 프로그레스바의 setValue 슬롯에 연결
        self.ui.setupUi(self)
        self.progress_updated.connect(self.ui.progressBar_loading.setValue)

    def update_progress(self, value):
        self.progress_updated.emit(value)

