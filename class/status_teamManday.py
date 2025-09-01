from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import status_teamManday_UI

class teamMandayDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = status_teamManday_UI.Ui_Form_allTeamManday()
        self.ui.setupUi(self)