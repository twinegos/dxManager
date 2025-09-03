from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import task_info_UI


class TaskInfoDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = task_info_UI.Ui_Form()
        self.ui.setupUi(self)

        self.ui.line.setStyleSheet("QFrame { background-color: #3c3c3c; height: 1px; border: none;}")