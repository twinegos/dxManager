# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editMember_dialoglnhgbl.ui'
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
        teamEdit_frm.resize(472, 360)
        teamEdit_frm.setMinimumSize(QSize(472, 0))
        teamEdit_frm.setMaximumSize(QSize(472, 100000))
        self.verticalLayout_2 = QVBoxLayout(teamEdit_frm)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.memberAdd_layout = QHBoxLayout()
        self.memberAdd_layout.setObjectName(u"memberAdd_layout")
        self.part_label = QLabel(teamEdit_frm)
        self.part_label.setObjectName(u"part_label")

        self.memberAdd_layout.addWidget(self.part_label)

        self.part_comboBox = QComboBox(teamEdit_frm)
        self.part_comboBox.setObjectName(u"part_comboBox")
        self.part_comboBox.setMinimumSize(QSize(100, 0))
        self.part_comboBox.setMaximumSize(QSize(100, 36))
        font = QFont()
        font.setPointSize(11)
        self.part_comboBox.setFont(font)
        self.part_comboBox.setIconSize(QSize(16, 16))

        self.memberAdd_layout.addWidget(self.part_comboBox)

        self.Name_label = QLabel(teamEdit_frm)
        self.Name_label.setObjectName(u"Name_label")

        self.memberAdd_layout.addWidget(self.Name_label)

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
        self.member_listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.member_listView.setSelectionMode(QAbstractItemView.SingleSelection)

        self.member_layout.addWidget(self.member_listView)

        self.memberEdit_layout = QVBoxLayout()
        self.memberEdit_layout.setObjectName(u"memberEdit_layout")
        self.remove_btn = QPushButton(teamEdit_frm)
        self.remove_btn.setObjectName(u"remove_btn")
        self.remove_btn.setMaximumSize(QSize(80, 36))

        self.memberEdit_layout.addWidget(self.remove_btn)

        self.memberEdit_spc_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.memberEdit_layout.addItem(self.memberEdit_spc_2)

        self.apply_btn = QPushButton(teamEdit_frm)
        self.apply_btn.setObjectName(u"apply_btn")
        self.apply_btn.setMaximumSize(QSize(80, 36))

        self.memberEdit_layout.addWidget(self.apply_btn)


        self.member_layout.addLayout(self.memberEdit_layout)


        self.verticalLayout_2.addLayout(self.member_layout)


        self.retranslateUi(teamEdit_frm)

        QMetaObject.connectSlotsByName(teamEdit_frm)
    # setupUi

    def retranslateUi(self, teamEdit_frm):
        teamEdit_frm.setWindowTitle(QCoreApplication.translate("teamEdit_frm", u"Frame", None))
        self.part_label.setText(QCoreApplication.translate("teamEdit_frm", u"\ud30c\ud2b8", None))
        self.Name_label.setText(QCoreApplication.translate("teamEdit_frm", u"\uc774\ub984", None))
        self.add_btn.setText(QCoreApplication.translate("teamEdit_frm", u"Add", None))
        self.remove_btn.setText(QCoreApplication.translate("teamEdit_frm", u"Del", None))
        self.apply_btn.setText(QCoreApplication.translate("teamEdit_frm", u"Apply", None))
    # retranslateUi

