from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import projManday_UI

class projManday_(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = projManday_UI.Ui_Form_mandayStatus()
        self.ui.setupUi(self)