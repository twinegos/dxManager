# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerKwXfTH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


# import Drag and Drop ListView class
ListViewPath = os.path.dirname(os.path.abspath(__file__)) + "/class"
sys.path.append(ListViewPath)
import dragDropListView as DD



class DayScheduleUI(object):
    def __init__(self):
        self.daySchedule_frame = QFrame()

        self.daySchedule_frame.setObjectName(u"daySchedule_frame")
        self.daySchedule_frame.resize(1404, 771)
        self.horizontalLayout = QHBoxLayout(self.daySchedule_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.comboBox_year = QComboBox(self.daySchedule_frame)
        self.comboBox_year.setObjectName(u"comboBox_year")

        self.horizontalLayout_5.addWidget(self.comboBox_year)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(70, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.backwardDayButton = QPushButton(self.daySchedule_frame)
        self.backwardDayButton.setObjectName(u"backwardDayButton")
        self.backwardDayButton.setText("<")


        self.horizontalLayout_3.addWidget(self.backwardDayButton)

        self.comboBox_month = QComboBox(self.daySchedule_frame)
        self.comboBox_month.setObjectName(u"comboBox_month")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_month.sizePolicy().hasHeightForWidth())
        self.comboBox_month.setSizePolicy(sizePolicy)
        self.comboBox_month.setMinimumSize(QSize(100, 80))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_month.setFont(font)

        self.horizontalLayout_3.addWidget(self.comboBox_month)

        self.comboBox_day = QComboBox(self.daySchedule_frame)
        self.comboBox_day.setObjectName(u"comboBox_day")
        self.comboBox_day.setMinimumSize(QSize(150, 80))
        font1 = QFont()
        font1.setPointSize(25)
        font1.setBold(True)
        font1.setWeight(75)
        self.comboBox_day.setFont(font1)

        self.horizontalLayout_3.addWidget(self.comboBox_day, 0, Qt.AlignHCenter)

        self.forwardDayButton = QPushButton(self.daySchedule_frame)
        self.forwardDayButton.setObjectName(u"forwardDayButton")
        self.forwardDayButton.setText(">")


        self.horizontalLayout_3.addWidget(self.forwardDayButton)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalSpacer_3 = QSpacerItem(20, 42, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_day_1 = QLabel(self.daySchedule_frame)
        self.label_day_1.setObjectName(u"label_day_1")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_day_1.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_day_1, 0, Qt.AlignHCenter)

        self.listView_day1 = DD.dropListView(self.daySchedule_frame)
        self.listView_day1.setObjectName(u"listView_day1")
        font3 = QFont()
        font3.setPointSize(11)
        self.listView_day1.setFont(font3)

        self.verticalLayout_4.addWidget(self.listView_day1)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_day_2 = QLabel(self.daySchedule_frame)
        self.label_day_2.setObjectName(u"label_day_2")
        self.label_day_2.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_day_2, 0, Qt.AlignHCenter)

        self.listView_day2 = DD.dropListView(self.daySchedule_frame)
        self.listView_day2.setObjectName(u"listView_day2")
        self.listView_day2.setFrameShape(QFrame.StyledPanel)
        self.listView_day2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.listView_day2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_day_3 = QLabel(self.daySchedule_frame)
        self.label_day_3.setObjectName(u"label_day_3")
        self.label_day_3.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_day_3, 0, Qt.AlignHCenter)

        self.listView_day3 = DD.dropListView(self.daySchedule_frame)
        self.listView_day3.setObjectName(u"listView_day3")
        self.listView_day3.setDragEnabled(True)
        self.listView_day3.setDragDropMode(QAbstractItemView.DropOnly)

        self.verticalLayout_7.addWidget(self.listView_day3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_day_4 = QLabel(self.daySchedule_frame)
        self.label_day_4.setObjectName(u"label_day_4")
        self.label_day_4.setFont(font2)

        self.verticalLayout_6.addWidget(self.label_day_4, 0, Qt.AlignHCenter)

        self.listView_day4 = DD.dropListView(self.daySchedule_frame)
        self.listView_day4.setObjectName(u"listView_day4")

        self.verticalLayout_6.addWidget(self.listView_day4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_day_5 = QLabel(self.daySchedule_frame)
        self.label_day_5.setObjectName(u"label_day_5")
        self.label_day_5.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_day_5, 0, Qt.AlignHCenter)

        self.listView_day5 = DD.dropListView(self.daySchedule_frame)
        self.listView_day5.setObjectName(u"listView_day5")

        self.verticalLayout_5.addWidget(self.listView_day5)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout.addLayout(self.verticalLayout_2)


        #self.retranslateUi(self.daySchedule_frame)

        #QMetaObject.connectSlotsByName(self.daySchedule_frame)







"""
    def retranslateUi(self, daySchedule_frame):
        daySchedule_frame.setWindowTitle(QCoreApplication.translate("daySchedule_frame", u"Frame", None))
        self.backwardDayButton.setText(QCoreApplication.translate("daySchedule_frame", u"<", None))
        self.forwardDayButton.setText(QCoreApplication.translate("daySchedule_frame", u">", None))
        self.label_day_1.setText(QCoreApplication.translate("daySchedule_frame", u"TextLabel", None))
        self.label_day_2.setText(QCoreApplication.translate("daySchedule_frame", u"TextLabel", None))
        self.label_day_3.setText(QCoreApplication.translate("daySchedule_frame", u"TextLabel", None))
        self.label_day_4.setText(QCoreApplication.translate("daySchedule_frame", u"TextLabel", None))
        self.label_day_5.setText(QCoreApplication.translate("daySchedule_frame", u"TextLabel", None))
    # retranslateUi
"""
