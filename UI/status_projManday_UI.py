# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_status_all_projMandayCxwvhM.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form_allManday(object):
    def setupUi(self, Form_allManday):
        if not Form_allManday.objectName():
            Form_allManday.setObjectName(u"Form_allManday")
        Form_allManday.resize(983, 154)
        self.verticalLayout_2 = QVBoxLayout(Form_allManday)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.v_Layout_allManday = QVBoxLayout()
        self.v_Layout_allManday.setObjectName(u"v_Layout_allManday")
        self.h_layout_name = QHBoxLayout()
        self.h_layout_name.setObjectName(u"h_layout_name")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.h_layout_name.addItem(self.horizontalSpacer_4)

        self.label_team = QLabel(Form_allManday)
        self.label_team.setObjectName(u"label_team")
        self.label_team.setMaximumSize(QSize(150, 16777215))
        self.label_team.setAlignment(Qt.AlignCenter)

        self.h_layout_name.addWidget(self.label_team)

        self.label_name = QLabel(Form_allManday)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setMaximumSize(QSize(300, 16777215))
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.h_layout_name.addWidget(self.label_name)

        self.button_teamWorkload = QPushButton(Form_allManday)
        self.button_teamWorkload.setObjectName(u"button_teamWorkload")
        self.button_teamWorkload.setMinimumSize(QSize(50, 0))
        self.button_teamWorkload.setMaximumSize(QSize(50, 16777215))
        self.button_teamWorkload.setAutoDefault(False)
        self.button_teamWorkload.setFlat(False)

        self.h_layout_name.addWidget(self.button_teamWorkload)

        self.horizontalSpacer = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.h_layout_name.addItem(self.horizontalSpacer)

        self.frame_periodWorkload = QFrame(Form_allManday)
        self.frame_periodWorkload.setObjectName(u"frame_periodWorkload")
        self.frame_periodWorkload.setFrameShape(QFrame.StyledPanel)
        self.frame_periodWorkload.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_periodWorkload)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_allTasks = QLabel(self.frame_periodWorkload)
        self.label_allTasks.setObjectName(u"label_allTasks")
        self.label_allTasks.setMinimumSize(QSize(70, 0))
        font1 = QFont()
        font1.setPointSize(25)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_allTasks.setFont(font1)
        self.label_allTasks.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.label_allTasks.setMargin(0)

        self.horizontalLayout.addWidget(self.label_allTasks)

        self.v_Layout_periodWorkload_1 = QVBoxLayout()
        self.v_Layout_periodWorkload_1.setSpacing(1)
        self.v_Layout_periodWorkload_1.setObjectName(u"v_Layout_periodWorkload_1")
        self.label_QTasks = QLabel(self.frame_periodWorkload)
        self.label_QTasks.setObjectName(u"label_QTasks")

        self.v_Layout_periodWorkload_1.addWidget(self.label_QTasks)

        self.progressBar_quarterTasks = QProgressBar(self.frame_periodWorkload)
        self.progressBar_quarterTasks.setObjectName(u"progressBar_quarterTasks")
        self.progressBar_quarterTasks.setValue(24)
        self.progressBar_quarterTasks.setTextVisible(False)

        self.v_Layout_periodWorkload_1.addWidget(self.progressBar_quarterTasks)


        self.horizontalLayout.addLayout(self.v_Layout_periodWorkload_1)

        self.label_wip_allTasks = QLabel(self.frame_periodWorkload)
        self.label_wip_allTasks.setObjectName(u"label_wip_allTasks")
        self.label_wip_allTasks.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.horizontalLayout.addWidget(self.label_wip_allTasks)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label_allMandays = QLabel(self.frame_periodWorkload)
        self.label_allMandays.setObjectName(u"label_allMandays")
        self.label_allMandays.setMinimumSize(QSize(70, 0))
        self.label_allMandays.setFont(font1)
        self.label_allMandays.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.horizontalLayout.addWidget(self.label_allMandays)

        self.v_Layout_periodWorkload_2 = QVBoxLayout()
        self.v_Layout_periodWorkload_2.setSpacing(1)
        self.v_Layout_periodWorkload_2.setObjectName(u"v_Layout_periodWorkload_2")
        self.label_Qmandays = QLabel(self.frame_periodWorkload)
        self.label_Qmandays.setObjectName(u"label_Qmandays")

        self.v_Layout_periodWorkload_2.addWidget(self.label_Qmandays)

        self.progressBar_quarterMandays = QProgressBar(self.frame_periodWorkload)
        self.progressBar_quarterMandays.setObjectName(u"progressBar_quarterMandays")
        self.progressBar_quarterMandays.setValue(24)
        self.progressBar_quarterMandays.setTextVisible(False)

        self.v_Layout_periodWorkload_2.addWidget(self.progressBar_quarterMandays)


        self.horizontalLayout.addLayout(self.v_Layout_periodWorkload_2)

        self.label_used_allMandays = QLabel(self.frame_periodWorkload)
        self.label_used_allMandays.setObjectName(u"label_used_allMandays")
        self.label_used_allMandays.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.horizontalLayout.addWidget(self.label_used_allMandays)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.h_layout_name.addWidget(self.frame_periodWorkload)


        self.v_Layout_allManday.addLayout(self.h_layout_name)

        self.v_Spacer_allManday = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.v_Layout_allManday.addItem(self.v_Spacer_allManday)

        self.line = QFrame(Form_allManday)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.v_Layout_allManday.addWidget(self.line)

        self.checkBox_visivilityCompletedProj = QCheckBox(Form_allManday)
        self.checkBox_visivilityCompletedProj.setObjectName(u"checkBox_visivilityCompletedProj")

        self.v_Layout_allManday.addWidget(self.checkBox_visivilityCompletedProj, 0, Qt.AlignRight)


        self.verticalLayout_2.addLayout(self.v_Layout_allManday)


        self.retranslateUi(Form_allManday)

        self.button_teamWorkload.setDefault(False)


        QMetaObject.connectSlotsByName(Form_allManday)
    # setupUi

    def retranslateUi(self, Form_allManday):
        Form_allManday.setWindowTitle(QCoreApplication.translate("Form_allManday", u"Form", None))
        self.label_team.setText(QCoreApplication.translate("Form_allManday", u"Team", None))
        self.label_name.setText(QCoreApplication.translate("Form_allManday", u"Name", None))
        self.button_teamWorkload.setText(QCoreApplication.translate("Form_allManday", u"Team", None))
        self.label_allTasks.setText(QCoreApplication.translate("Form_allManday", u"Tasks", None))
        self.label_QTasks.setText(QCoreApplication.translate("Form_allManday", u"Tasks", None))
        self.label_wip_allTasks.setText(QCoreApplication.translate("Form_allManday", u"wip/all", None))
        self.label_allMandays.setText(QCoreApplication.translate("Form_allManday", u"days", None))
        self.label_Qmandays.setText(QCoreApplication.translate("Form_allManday", u"Mandays", None))
        self.label_used_allMandays.setText(QCoreApplication.translate("Form_allManday", u"used/allMD", None))
        self.checkBox_visivilityCompletedProj.setText(QCoreApplication.translate("Form_allManday", u"Completed Project", None))
    # retranslateUi

