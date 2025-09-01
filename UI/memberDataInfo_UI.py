# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerPuLZgk.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_workData_frm(QWidget):

    def __init__(self):
        super().__init__()

        self.workData_frm = QFrame()
        self.workData_frm.resize(846, 536)
        self.verticalLayout = QVBoxLayout(self.workData_frm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.workData_tableView = QTableView(self.workData_frm)
        self.workData_tableView.setObjectName(u"workData_tableView")

        self.verticalLayout.addWidget(self.workData_tableView)


        #self.retranslateUi(workData_frm)

        #QMetaObject.connectSlotsByName(workData_frm)
    # setupUi

    #def retranslateUi(self, workData_frm):
    #    workData_frm.setWindowTitle(QCoreApplication.translate("workData_frm", u"Frame", None))
    # retranslateUi