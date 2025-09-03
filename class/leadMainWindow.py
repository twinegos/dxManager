from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import os
import sys
import json
#import EditMemberDialog_UI

currentPath = os.path.dirname(os.path.abspath(__file__))
Path_UI = os.path.dirname(currentPath) + "/UI"

sys.path.append(currentPath)
import dragDropListView as DD

sys.path.append(Path_UI)
import leadMainWindow_UI


class LeadMainWindow(QMainWindow):
    def __init__(self):
        super(LeadMainWindow, self).__init__()

        self.ui_leadWin = leadMainWindow_UI.Ui_MainWindow()
        self.ui_leadWin.setupUi(self)        



        self.ui_leadWin.shotListView = DD.DragListView(self.ui_leadWin.leftSide_frame)
