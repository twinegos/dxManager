# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_mandaysCGFMUb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog_editMandays(object):
    def setupUi(self, Dialog_editMandays):
        if not Dialog_editMandays.objectName():
            Dialog_editMandays.setObjectName(u"Dialog_editMandays")
        Dialog_editMandays.resize(720, 576)
        self.verticalLayout = QVBoxLayout(Dialog_editMandays)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.v_Layout_editMandays = QVBoxLayout()
        self.v_Layout_editMandays.setObjectName(u"v_Layout_editMandays")
        self.table_editMandays = QTableWidget(Dialog_editMandays)
        self.table_editMandays.setObjectName(u"table_editMandays")
        font = QFont()
        font.setPointSize(10)
        self.table_editMandays.setFont(font)
        self.table_editMandays.setSortingEnabled(True)
        self.table_editMandays.setRowCount(0)
        self.table_editMandays.setColumnCount(0)
        self.table_editMandays.horizontalHeader().setVisible(True)
        self.table_editMandays.horizontalHeader().setCascadingSectionResizes(False)
        self.table_editMandays.verticalHeader().setProperty("showSortIndicator", True)

        self.v_Layout_editMandays.addWidget(self.table_editMandays)

        self.h_Layout_button = QHBoxLayout()
        self.h_Layout_button.setObjectName(u"h_Layout_button")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.h_Layout_button.addItem(self.horizontalSpacer)

        self.Button_save = QPushButton(Dialog_editMandays)
        self.Button_save.setObjectName(u"Button_save")

        self.h_Layout_button.addWidget(self.Button_save)

        self.Button_export = QPushButton(Dialog_editMandays)
        self.Button_export.setObjectName(u"Button_export")

        self.h_Layout_button.addWidget(self.Button_export)


        self.v_Layout_editMandays.addLayout(self.h_Layout_button)


        self.verticalLayout.addLayout(self.v_Layout_editMandays)


        self.retranslateUi(Dialog_editMandays)

        QMetaObject.connectSlotsByName(Dialog_editMandays)
    # setupUi

    def retranslateUi(self, Dialog_editMandays):
        Dialog_editMandays.setWindowTitle(QCoreApplication.translate("Dialog_editMandays", u"Adjust Mandays", None))
        self.Button_save.setText(QCoreApplication.translate("Dialog_editMandays", u"Apply", None))
        self.Button_export.setText(QCoreApplication.translate("Dialog_editMandays", u"Export", None))
    # retranslateUi

