# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_status_all_TeamMandayPudvVN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form_allTeamManday(object):
    def setupUi(self, Form_allTeamManday):
        if not Form_allTeamManday.objectName():
            Form_allTeamManday.setObjectName(u"Form_allTeamManday")
        Form_allTeamManday.resize(984, 635)
        Form_allTeamManday.setMinimumSize(QSize(980, 630))
        self.verticalLayout_2 = QVBoxLayout(Form_allTeamManday)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.v_Layout_allTeamManday = QVBoxLayout()
        self.v_Layout_allTeamManday.setObjectName(u"v_Layout_allTeamManday")
        self.h_layout_teamName = QHBoxLayout()
        self.h_layout_teamName.setSpacing(13)
        self.h_layout_teamName.setObjectName(u"h_layout_teamName")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.h_layout_teamName.addItem(self.horizontalSpacer_4)

        self.label_teamLeader = QLabel(Form_allTeamManday)
        self.label_teamLeader.setObjectName(u"label_teamLeader")
        self.label_teamLeader.setMaximumSize(QSize(150, 16777215))
        self.label_teamLeader.setAlignment(Qt.AlignCenter)

        self.h_layout_teamName.addWidget(self.label_teamLeader)

        self.label_teamName = QLabel(Form_allTeamManday)
        self.label_teamName.setObjectName(u"label_teamName")
        self.label_teamName.setMaximumSize(QSize(300, 16777215))
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_teamName.setFont(font)
        self.label_teamName.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.h_layout_teamName.addWidget(self.label_teamName)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.h_layout_teamName.addItem(self.horizontalSpacer)

        self.frame_periodTeamWorkload = QFrame(Form_allTeamManday)
        self.frame_periodTeamWorkload.setObjectName(u"frame_periodTeamWorkload")
        self.frame_periodTeamWorkload.setFrameShape(QFrame.StyledPanel)
        self.frame_periodTeamWorkload.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_periodTeamWorkload)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_allTasks = QLabel(self.frame_periodTeamWorkload)
        self.label_allTasks.setObjectName(u"label_allTasks")
        self.label_allTasks.setMinimumSize(QSize(40, 0))
        font1 = QFont()
        font1.setPointSize(25)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_allTasks.setFont(font1)
        self.label_allTasks.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_allTasks.setMargin(0)

        self.horizontalLayout.addWidget(self.label_allTasks)

        self.v_Layout_periodTeamWorkload_1 = QVBoxLayout()
        self.v_Layout_periodTeamWorkload_1.setSpacing(1)
        self.v_Layout_periodTeamWorkload_1.setObjectName(u"v_Layout_periodTeamWorkload_1")
        self.label_QteamTasks = QLabel(self.frame_periodTeamWorkload)
        self.label_QteamTasks.setObjectName(u"label_QteamTasks")

        self.v_Layout_periodTeamWorkload_1.addWidget(self.label_QteamTasks)

        self.progressBar_QteamTasks = QProgressBar(self.frame_periodTeamWorkload)
        self.progressBar_QteamTasks.setObjectName(u"progressBar_QteamTasks")
        self.progressBar_QteamTasks.setValue(24)
        self.progressBar_QteamTasks.setTextVisible(False)

        self.v_Layout_periodTeamWorkload_1.addWidget(self.progressBar_QteamTasks)


        self.horizontalLayout.addLayout(self.v_Layout_periodTeamWorkload_1)

        self.label_wip_allTeamTasks = QLabel(self.frame_periodTeamWorkload)
        self.label_wip_allTeamTasks.setObjectName(u"label_wip_allTeamTasks")
        self.label_wip_allTeamTasks.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.horizontalLayout.addWidget(self.label_wip_allTeamTasks)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label_allTeamMandays = QLabel(self.frame_periodTeamWorkload)
        self.label_allTeamMandays.setObjectName(u"label_allTeamMandays")
        self.label_allTeamMandays.setMinimumSize(QSize(40, 0))
        self.label_allTeamMandays.setFont(font1)
        self.label_allTeamMandays.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.horizontalLayout.addWidget(self.label_allTeamMandays)

        self.v_Layout_periodTeamWorkload_2 = QVBoxLayout()
        self.v_Layout_periodTeamWorkload_2.setSpacing(1)
        self.v_Layout_periodTeamWorkload_2.setObjectName(u"v_Layout_periodTeamWorkload_2")
        self.label_QteamMandays = QLabel(self.frame_periodTeamWorkload)
        self.label_QteamMandays.setObjectName(u"label_QteamMandays")

        self.v_Layout_periodTeamWorkload_2.addWidget(self.label_QteamMandays)

        self.progressBar_QteamMandays = QProgressBar(self.frame_periodTeamWorkload)
        self.progressBar_QteamMandays.setObjectName(u"progressBar_QteamMandays")
        self.progressBar_QteamMandays.setValue(24)
        self.progressBar_QteamMandays.setTextVisible(False)

        self.v_Layout_periodTeamWorkload_2.addWidget(self.progressBar_QteamMandays)


        self.horizontalLayout.addLayout(self.v_Layout_periodTeamWorkload_2)

        self.label_used_allTeamMandays = QLabel(self.frame_periodTeamWorkload)
        self.label_used_allTeamMandays.setObjectName(u"label_used_allTeamMandays")
        self.label_used_allTeamMandays.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.horizontalLayout.addWidget(self.label_used_allTeamMandays)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.h_layout_teamName.addWidget(self.frame_periodTeamWorkload)


        self.v_Layout_allTeamManday.addLayout(self.h_layout_teamName)

        self.verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.v_Layout_allTeamManday.addItem(self.verticalSpacer)

        self.line = QFrame(Form_allTeamManday)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.v_Layout_allTeamManday.addWidget(self.line)

        self.checkBox_visivilityCompletedProj = QCheckBox(Form_allTeamManday)
        self.checkBox_visivilityCompletedProj.setObjectName(u"checkBox_visivilityCompletedProj")

        self.v_Layout_allTeamManday.addWidget(self.checkBox_visivilityCompletedProj, 0, Qt.AlignRight)

        self.scrollArea_teamManday = QScrollArea(Form_allTeamManday)
        self.scrollArea_teamManday.setObjectName(u"scrollArea_teamManday")
        self.scrollArea_teamManday.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 966, 476))
        self.v_Layout_scrollArea = QVBoxLayout(self.scrollAreaWidgetContents)
        self.v_Layout_scrollArea.setObjectName(u"v_Layout_scrollArea")
        self.scrollArea_teamManday.setWidget(self.scrollAreaWidgetContents)

        self.v_Layout_allTeamManday.addWidget(self.scrollArea_teamManday)


        self.verticalLayout_2.addLayout(self.v_Layout_allTeamManday)


        self.retranslateUi(Form_allTeamManday)

        QMetaObject.connectSlotsByName(Form_allTeamManday)
    # setupUi

    def retranslateUi(self, Form_allTeamManday):
        Form_allTeamManday.setWindowTitle(QCoreApplication.translate("Form_allTeamManday", u"Form", None))
        self.label_teamLeader.setText(QCoreApplication.translate("Form_allTeamManday", u"Leader", None))
        self.label_teamName.setText(QCoreApplication.translate("Form_allTeamManday", u"Team", None))
        self.label_allTasks.setText(QCoreApplication.translate("Form_allTeamManday", u"Tasks", None))
        self.label_QteamTasks.setText(QCoreApplication.translate("Form_allTeamManday", u"Tasks", None))
        self.label_wip_allTeamTasks.setText(QCoreApplication.translate("Form_allTeamManday", u"wip/all", None))
        self.label_allTeamMandays.setText(QCoreApplication.translate("Form_allTeamManday", u"days", None))
        self.label_QteamMandays.setText(QCoreApplication.translate("Form_allTeamManday", u"Mandays", None))
        self.label_used_allTeamMandays.setText(QCoreApplication.translate("Form_allTeamManday", u"used/allMD", None))
        self.checkBox_visivilityCompletedProj.setText(QCoreApplication.translate("Form_allTeamManday", u"Completed Project", None))
    # retranslateUi

