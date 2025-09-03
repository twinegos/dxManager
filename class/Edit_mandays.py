from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import edit_mandays_UI

class EditMandays(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = edit_mandays_UI.Ui_Dialog_editMandays()
        self.ui.setupUi(self)