# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editMember_dialogGwiySr.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_teamEdit_frm(object):
    def setupUi(self, teamEdit_frm):
        if not teamEdit_frm.objectName():
            teamEdit_frm.setObjectName(u"teamEdit_frm")
        teamEdit_frm.resize(315, 360)
        teamEdit_frm.setMinimumSize(QSize(315, 360))
        teamEdit_frm.setMaximumSize(QSize(315, 360))
        self.verticalLayout_2 = QVBoxLayout(teamEdit_frm)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.memberAdd_layout = QHBoxLayout()
        self.memberAdd_layout.setObjectName(u"memberAdd_layout")
        self.addLineEdit = QLineEdit(teamEdit_frm)
        self.addLineEdit.setObjectName(u"addLineEdit")

        self.memberAdd_layout.addWidget(self.addLineEdit)

        self.add_btn = QPushButton(teamEdit_frm)
        self.add_btn.setObjectName(u"add_btn")

        self.memberAdd_layout.addWidget(self.add_btn)


        self.verticalLayout_2.addLayout(self.memberAdd_layout)

        self.member_layout = QHBoxLayout()
        self.member_layout.setObjectName(u"member_layout")
        self.member_listView = QListView(teamEdit_frm)
        self.member_listView.setObjectName(u"member_listView")

        self.member_layout.addWidget(self.member_listView)

        self.memberEdit_layout = QVBoxLayout()
        self.memberEdit_layout.setObjectName(u"memberEdit_layout")
        self.rename_btn = QPushButton(teamEdit_frm)
        self.rename_btn.setObjectName(u"rename_btn")

        self.memberEdit_layout.addWidget(self.rename_btn)

        self.remove_btn = QPushButton(teamEdit_frm)
        self.remove_btn.setObjectName(u"remove_btn")

        self.memberEdit_layout.addWidget(self.remove_btn)

        self.memberEdit_spc_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.memberEdit_layout.addItem(self.memberEdit_spc_2)


        self.member_layout.addLayout(self.memberEdit_layout)


        self.verticalLayout_2.addLayout(self.member_layout)


        self.retranslateUi(teamEdit_frm)

        QMetaObject.connectSlotsByName(teamEdit_frm)
    # setupUi

    def retranslateUi(self, teamEdit_frm):
        teamEdit_frm.setWindowTitle(QCoreApplication.translate("teamEdit_frm", u"Frame", None))
        self.add_btn.setText(QCoreApplication.translate("teamEdit_frm", u"Add", None))
        self.rename_btn.setText(QCoreApplication.translate("teamEdit_frm", u"Rename", None))
        self.remove_btn.setText(QCoreApplication.translate("teamEdit_frm", u"Del", None))
    # retranslateUi

