from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import status_projManday_UI

class projMandayDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = status_projManday_UI.Ui_Form_allManday()
        self.ui.setupUi(self)